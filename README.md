# Computer Vision and Robotics Lab — website

> 🇪🇸 Guía de publicación en GitHub Pages y dominio propio: [README.es.md](README.es.md)

Website of the Computer Vision and Robotics Lab (CVR Lab), University of Granada.
Built with [Hugo](https://gohugo.io) and the [HugoBlox kit](https://github.com/HugoBlox/kit)
(Tailwind CSS), published to GitHub Pages at <https://cvr-lab.github.io/>.

This is a prototype migrated from the Wowchemy 5 site currently served at
<https://www.ugr.es/~cvrlab/> (source: `fbarranco/starter-research-group`).

## Where things live

| What | Where |
| --- | --- |
| Home page sections (hero, about, projects, news) | `content/_index.md` |
| Projects (one folder each, `featured.jpg` is the card image) | `content/projects/<name>/index.md` |
| Publications (one folder each, with `cite.bib`) | `content/publications/<key>/index.md` |
| News posts | `content/blog/<date-slug>/index.md` |
| People page layout and groups | `content/people/index.md` |
| Person profiles | `data/authors/<slug>.yaml` + photo in `assets/media/authors/<slug>.jpg` |
| Contact page | `content/contact/index.md` |
| Site name, theme, header/footer | `config/_default/params.yaml` |
| Menu | `config/_default/menus.yaml` |
| Hugo version used by CI | `hugoblox.yaml` (`build.hugo_version`) |
| Project card and research-area card designs (overrides of kit's `portfolio` and `focus-areas` blocks) | `layouts/_partials/hbx/blocks/<block>/block.html` |
| Site font (Roboto, selected by `typography.pack` in `params.yaml`) | `data/fonts/roboto.yaml` |
| Header: logo, wordmark, menu (override of kit's navbar) | `layouts/_partials/components/headers/navbar.html` |
| Page title band on Projects, People, News, Publications, Contact (text from each page's `lead:` front matter) | `layouts/_partials/cvr/page_header.html`, used by `layouts/landing/*.html` and `layouts/list.html` |
| Publications page (grouped by year, type filter) | `layouts/publications/list.html` |
| Site CSS (header, publications, section spacing) | `assets/css/custom.css` |

### Adding a person

Create `data/authors/<slug>.yaml`, where `<slug>` is the person's name lower-cased with
dashes (`Jane Doe` → `jane-doe`). Use the same display name in a publication's or
project's `authors:` list and it links to the profile automatically. Put
the person in one of the groups listed in `content/people/index.md` via `user_groups`,
and use `weight` to order people inside a group.

### Adding a publication

Copy an existing folder in `content/publications/`, or add the BibTeX entry to a
`publications.bib` file at the repo root: the *Import Publications From Bibtex*
workflow converts it and opens a pull request.

## Local development

Requirements: Hugo **extended 0.161.1** (see the note below), Go, and Node.js 22 with pnpm or npm.

```sh
pnpm install          # or: npm install
hugo server           # http://localhost:1313/
```

Production build, including the search index:

```sh
hugo --minify && npx pagefind --site public
```

> **Hugo version:** the pinned HugoBlox module needs Hugo ≥ 0.161.1, and Hugo 0.162.0
> currently fails on pages that have links (`assignment to entry in nil map` in
> `functions/build_links.html`). Keep `hugoblox.yaml` on 0.161.1 until an upgrade PR
> builds cleanly.

## Deployment

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and
publishes it to GitHub Pages. One-time repository setup: **Settings → Pages → Build and
deployment → Source: GitHub Actions**.

`.github/workflows/upgrade.yml` opens a weekly pull request that bumps the HugoBlox
modules; the build workflow checks it before you merge.
