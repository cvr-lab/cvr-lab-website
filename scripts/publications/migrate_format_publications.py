#!/usr/bin/env python3
"""Migra el front matter antiguo de las publicaciones al formato HugoBlox actual."""

import argparse
from pathlib import Path
from ruamel.yaml import YAML


yaml = YAML(typ="rt")
yaml.preserve_quotes = True
yaml.width = 4096
yaml.indent(mapping=2, sequence=4, offset=2)


def migrate(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return False

    parts = text.split("---", 2)
    if len(parts) != 3:
        return False

    data = yaml.load(parts[1]) or {}
    changed = False

    # 1. publication: "Nombre de revista"
    #    -> publication: {name: "Nombre de revista"}
    publication = data.get("publication")

    if isinstance(publication, str):
        data["publication"] = {"name": publication}
        changed = True
    elif publication is None:
        data["publication"] = {}
        changed = True

    publication = data["publication"]

    # 2. Mover los metadatos bibliográficos al objeto publication.
    for old, new in (
        ("volume", "volume"),
        ("issue", "issue"),
        ("pages", "pages"),
        ("publisher", "publisher"),
    ):
        if old in data:
            if new not in publication:
                publication[new] = data[old]
            del data[old]
            changed = True

    # 3. doi -> hugoblox.ids.doi
    if "doi" in data:
        doi = data.pop("doi")

        hugoblox = data.setdefault("hugoblox", {})
        ids = hugoblox.setdefault("ids", {})

        if "doi" in ids and ids["doi"] != doi:
            raise ValueError(
                f"{path}: hay dos DOI diferentes en el front matter"
            )

        ids["doi"] = doi
        changed = True

    if changed:
        from io import StringIO

        output = StringIO()
        yaml.dump(data, output)

        new_text = "---\n" + output.getvalue() + "---" + parts[2]
        path.write_text(new_text, encoding="utf-8")

    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory",
        nargs="?",
        default="content/publications",
    )
    args = parser.parse_args()

    directory = Path(args.directory)
    files = sorted(directory.glob("*/index.md"))

    migrated = 0

    for path in files:
        if migrate(path):
            print(f"Migrada: {path}")
            migrated += 1

    print(f"\nPublicaciones revisadas: {len(files)}")
    print(f"Publicaciones migradas: {migrated}")


if __name__ == "__main__":
    main()