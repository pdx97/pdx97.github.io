# Prakhar Dixit's website

Static HTML portfolio hosted by GitHub Pages. No Node dependencies or build step is required for the website.

## Editing

- Shared design: `assets/css/style.css`.
- Shared accessible navigation behavior: `assets/js/site.js`.
- Main pages: `index.html`, `publications.html`, `experience.html`, `projects.html`, `honors.html`, `education.html`, `contact.html`.
- `index2.html` forwards old section bookmarks to the corresponding current page.
- Update `data/ism.json`, then run `python scripts/sync_ism.py` to synchronize the ISM paper across all relevant pages. The generated HTML is committed, readable by search engines, and works without JavaScript.
- The current CV is `Docs/Prakhar_Dixit_CV.pdf`. Historical PDFs are retained but are no longer linked by the site.

## Validation

Run `python scripts/validate_site.py`, `node --check assets/js/site.js`, and `node --check assets/js/legacy.js`.

To regenerate the CV, install `beautifulsoup4` and `reportlab` in your Python environment, install the DejaVu Sans fonts (the generator uses `/usr/share/fonts/truetype/dejavu/`), and run `python scripts/build_cv.py` after synchronizing ISM. Review the generated PDF before committing it. The CV uses the website content rather than a second manually maintained publication list.

## Contact

The contact page retains the existing Formspree endpoint. Email delivery and ownership need to be checked by the site owner; local validation does not submit messages.

See `SITE_REVIEW.md` for the renewal findings and outstanding content questions.
