# Prakhar Dixit's website

Static academic homepage hosted by GitHub Pages. No build step.

## Editing

- Shared design: `assets/css/style.css` (light/dark via `prefers-color-scheme`).
- Mobile navigation behavior: `assets/js/site.js`.
- Pages: `index.html` (about, news, selected publications, service), `publications.html`, `experience.html`, `education.html`, `projects.html`, `honors.html` (talks, awards, service), `contact.html`.
- `index2.html` forwards old section bookmarks to the corresponding current page.
- The CV linked everywhere is `Docs/Prakhar_Dixit_CV.pdf`. To update it, replace that file. Older PDFs in `Docs/` are kept but no longer linked.

## Adding a publication

Copy an existing `<li class="pub">` block in `publications.html` (and in `index.html` under "Selected Publications" if it should be featured). Wrap your own name in `<span class="me">`, and add a news item on the home page.
