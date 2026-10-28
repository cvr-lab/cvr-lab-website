"""Migrate content from the old Wowchemy 5 site to the HugoBlox kit layout.

usage: python3 -I migrate.py OLD_REPO NEW_SITE
"""
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import yaml

OLD = Path(sys.argv[1])
NEW = Path(sys.argv[2])

PUB_TYPES = {"1": "paper-conference", "2": "article-journal"}

# Normalise inconsistent spellings of author names found in the old content.
NAME_FIX = {
    "admin": "Francisco Barranco",
    "Javier Diaz": "Javier Díaz",
    "Cornelia Fermuller": "Cornelia Fermüller",
}

# Profiles whose old bio/interests were untouched Wowchemy demo text.
AUTHOR_FIX = {
    "juan-isern": {
        "bio": "Juan Isern is a PhD Student in Computer Engineering at the University of Granada.",
        "interests": [],
    },
}

URL_FIELDS = {
    "url_pdf": "pdf", "url_code": "code", "url_dataset": "dataset",
    "url_poster": "poster", "url_slides": "slides", "url_source": "source",
    "url_video": "video", "url_project": "project",
}


LINK_LABELS = {
    "site": ("Website", "globe-alt"), "code": ("Code", "code-bracket"),
    "pdf": ("PDF", "document-text"), "dataset": ("Dataset", "circle-stack"),
    "poster": ("Poster", "presentation-chart-bar"), "slides": ("Slides", "presentation-chart-line"),
    "video": ("Video", "play-circle"), "source": ("Source", "document"),
    "project": ("Project", "folder"),
}


class Dumper(yaml.SafeDumper):
    pass


def _str(dumper, s):
    style = "|" if "\n" in s else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", s, style=style)


Dumper.add_representer(str, _str)


def dump(d):
    return yaml.dump(d, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=float('inf'))


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def read(path):
    text = path.read_text()
    # brainav/index.md lacks its closing delimiter and has an invalid month.
    if path.parent.name == "brainav":
        text = text.replace('date: "2023-19-01', 'date: "2023-01-19')
        if text.count("\n---\n") < 1:
            text = text.replace('url_video: ""\n', 'url_video: ""\n---\n', 1)
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body.strip() + "\n"


def write(path, fm, body=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + dump(fm) + "---\n" + (("\n" + body) if body.strip() else ""))


def fix_name(n):
    n = n.strip()
    return NAME_FIX.get(n, n)


def plain(md):
    """Markdown paragraph -> plain text (team cards print the bio raw)."""
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    return " ".join(md.split())


def legacy_links(d):
    """Collect old `links`, `url_*` and `external_link` into kit's typed list."""
    out = []
    if d.get("external_link"):
        out.append({"type": "site", "url": d["external_link"]})
    for link in d.get("links") or []:
        url = link.get("url", "")
        if not url or url == "#":
            continue
        typ = "code" if link.get("icon") == "github" else "custom"
        entry = {"type": typ, "url": url}
        if typ == "custom":
            entry["label"] = link.get("name", "Link")
        out.append(entry)
    for field, typ in URL_FIELDS.items():
        url = d.get(field)
        if url and url != "#":
            out.append({"type": typ, "url": url})
    # A "Website" that is just the code repository is dropped, and so is any repeated URL.
    other_urls = {link["url"] for link in out if link["type"] != "site"}
    out = [link for link in out if link["type"] != "site" or link["url"] not in other_urls]
    seen, uniq = set(), []
    for link in out:
        if link["url"] not in seen:
            seen.add(link["url"])
            uniq.append(link)
    # The portfolio card shows `label`/`icon` only, so give every link both.
    labels = set()
    for link in uniq:
        label, icon = LINK_LABELS.get(link["type"], ("Link", "link"))
        if link["type"] == "code" and "github.com" in link["url"]:
            icon = "brands/github"
        elif link["type"] == "code" and label in labels:
            # A second, non-GitHub "Code" link is a download mirror.
            label, icon = "Download", "arrow-down-tray"
        link.setdefault("label", label)
        link.setdefault("icon", icon)
        labels.add(link["label"])
    return uniq


def social_link(s):
    link = s["link"].strip()
    if " at " in link and "://" not in link:
        link = "mailto:" + link.replace("mailto:", "").replace(" at ", "@")
    if link.startswith("www."):
        link = "https://" + link
    icon = {
        "envelope": "at-symbol",
        "google-scholar": "academicons/google-scholar",
        "github": "brands/github",
        "linkedin": "brands/linkedin",
        "youtube": "brands/youtube",
    }.get(s["icon"], s["icon"])
    return {"icon": icon, "url": link}


def migrate_authors():
    """content/authors/<id>/_index.md -> data/authors/<slug>.yaml + avatar."""
    group_weight = {"Principal Investigators": 1, "Researchers": 2, "Alumni": 9}
    for idx in sorted((OLD / "content/authors").glob("*/_index.md")):
        d, body = read(idx)
        if idx.parent.name == "CVRLabGroup":
            continue  # group description, used as the homepage "about" text
        name = d["title"]
        slug = slugify(name)
        parts = name.split()
        out = {
            "schema": "hugoblox/author/v1",
            "slug": slug,
            "is_owner": bool(d.get("superuser")),
            "name": {"display": name, "given": parts[0], "family": " ".join(parts[1:])},
            "role": d.get("role", ""),
            "bio": plain(body) if body.strip() else d.get("bio", ""),
            "affiliations": [
                {"name": o["name"], **({"url": o["url"]} if o.get("url") else {})}
                for o in d.get("organizations") or []
            ],
            "links": [social_link(s) for s in d.get("social") or []],
            "interests": d.get("interests") or [],
            "education": [
                {"degree": c["course"], "institution": c["institution"],
                 "end": f"{c['year']}-12-31"}
                for c in (d.get("education") or {}).get("courses") or []
            ],
            "user_groups": d.get("user_groups") or [],
            "weight": group_weight.get((d.get("user_groups") or [""])[0], 5),
        }
        out.update(AUTHOR_FIX.get(slug, {}))
        (NEW / "data/authors").mkdir(parents=True, exist_ok=True)
        (NEW / f"data/authors/{slug}.yaml").write_text(dump(out))
        avatar = idx.parent / "avatar.jpg"
        if avatar.exists():
            dst = NEW / f"assets/media/authors/{slug}.jpg"
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(avatar, dst)


def migrate_publications():
    for idx in sorted((OLD / "content/publication").glob("*/index.md")):
        d, _ = read(idx)
        venue = re.sub(r"^In\s+", "", d.get("publication") or "").strip("* ")
        short = re.sub(r"^In\s+", "", d.get("publication_short") or "").strip("* ")
        out = {
            "title": d["title"],
            "authors": [fix_name(a) for a in d.get("authors") or [] if a and a.strip()],
            "date": d["date"],
            "publication_types": [PUB_TYPES.get(str(t), str(t)) for t in d.get("publication_types") or []],
            "publication": {"name": venue, **({"short_name": short} if short else {})},
            "abstract": d.get("abstract", ""),
        }
        if d.get("doi"):
            out["hugoblox"] = {"ids": {"doi": d["doi"]}}
        links = legacy_links(d)
        if links:
            out["links"] = links
        out["featured"] = bool(d.get("featured"))
        dst = NEW / "content/publications" / idx.parent.name.lower()
        write(dst / "index.md", out)  # old bodies were template placeholder text only
        for f in idx.parent.iterdir():
            if f.name != "index.md":
                shutil.copy(f, dst / f.name)


def fix_headings(body):
    """Drop a leading H1 that repeats the page title; demote the rest if H1s remain.

    The page layout already prints the title as the page's H1.
    """
    lines, in_code, heads = body.split("\n"), False, []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_code = not in_code
        elif not in_code and re.match(r"#+ ", line):
            heads.append(i)
    if heads and lines[heads[0]].startswith("# "):
        del lines[heads[0]]
        heads = [i - 1 for i in heads[1:]]
    if any(lines[i].startswith("# ") for i in heads):
        for i in heads:
            lines[i] = "#" + lines[i]
    return "\n".join(lines)


def migrate_projects():
    for idx in sorted((OLD / "content/project").glob("*/index.md")):
        d, body = read(idx)
        body = fix_headings(body)
        out = {"title": d["title"], "summary": d.get("summary", ""), "date": d["date"]}
        if d.get("lastmod"):
            out["lastmod"] = d["lastmod"]
        out["tags"] = d.get("tags") or []
        out["authors"] = [fix_name(a) for a in d.get("authors") or []]
        links = legacy_links(d)
        if links:
            out["links"] = links
        img = d.get("image") or {}
        out["image"] = {"caption": img.get("caption", ""), "focal_point": img.get("focal_point", "Smart")}
        dst = NEW / "content/projects" / idx.parent.name.lower()
        write(dst / "index.md", out, body)
        for f in idx.parent.iterdir():
            if f.name != "index.md":
                shutil.copy(f, dst / f.name)
        # Old figure shortcode found this in assets/media; Hugo's needs it in the bundle.
        if "basketview.jpg" in body:
            shutil.copy(OLD / "assets/media/basketview.jpg", dst / "basketview.jpg")


def migrate_posts():
    for idx in sorted((OLD / "content/post").glob("*/index.md")):
        d, body = read(idx)
        dst = NEW / "content/blog" / idx.parent.name.lower()
        write(dst / "index.md", {"title": d["title"], "date": d["date"]}, body)


if __name__ == "__main__":
    migrate_authors()
    migrate_publications()
    migrate_projects()
    migrate_posts()
    media = NEW / "assets/media"
    media.mkdir(parents=True, exist_ok=True)
    shutil.copy(OLD / "static/media/image.jpg", media / "hero.jpg")
    shutil.copy(OLD / "assets/images/icon.png", media / "icon.png")
    print("done")
