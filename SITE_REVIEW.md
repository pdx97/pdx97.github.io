# Website renewal review

## Corrected

- Education omitted the Honors navigation link. All seven main pages now expose the same navigation and identify the current page with `aria-current`.
- Experience and education content depended on animation JavaScript to become visible. All content is now visible by default, including when JavaScript is unavailable.
- Mobile navigation had incomplete keyboard behavior. The shared script adds Escape, outside-click, focus-out, and viewport-change handling, with a visible no-JavaScript navigation fallback.
- Reworked the dark portfolio with slate surfaces, mint accents, an editorial serif name, a larger portrait, readable body text, and responsive layouts. Replaced the alternating experience timeline and animated education staircase with straightforward layouts.
- Added skip links, main landmarks, semantic section headings, explicit keyboard focus, reduced-motion support, descriptive metadata, canonical URLs, and safer external-link attributes.
- Reused the bundled icon font instead of a third-party icon CDN.
- Replaced generic GitHub profile links for ScholarAgent and LLM AI Text with their verified repositories.
- Replaced the obsolete `index2.html` template (duplicate IDs, broken CV link, stale biography) with a compatibility redirect and no-JavaScript links.
- Added ISM to the homepage feature and news, publications, projects, UMBC research experience, education research reference, and the new downloadable CV. No award or presentation claim was invented for it.
- Rebuilt a four-page CV from website content, retaining historical PDFs. Current download links use the new CV.
- Corrected verified author ordering and workshop labels. In particular, ReProHRL, WildfireVLM, and the drone-navigation paper no longer incorrectly start their author lists with Prakhar.

## Publication evidence

- ISM: https://github.com/UMBC-Coral-Lab/ISM-Self-Improving-Strategy-Memory-for-Continual-Mathematical-Reasoning
- ISM workshop record: https://openreview.net/forum?id=5JK3t0YI5Z
- ISM preprint: https://arxiv.org/abs/2606.31191
- Honest Lying authors and workshop: https://arxiv.org/abs/2605.29463
- SBI-RAG authors and workshop: https://arxiv.org/abs/2410.13293
- ReProHRL authors and workshop: https://arxiv.org/abs/2308.08737
- WildfireVLM authors: https://arxiv.org/abs/2602.13305
- Drone paper authors: https://sim2real.github.io/assets/papers/2022/navardi.pdf
- RSS workshop: https://sim2real.github.io/

## Content requiring owner confirmation

1. **Exact requested citation:** Google Scholar blocked access to citation `oa-29J8AAAAJ:YOwf2qJgpHMC`. ISM is demonstrably missing from this repository and independently verified as Prakhar's paper. It was added as the likely intended paper, but the mapping from the supplied Scholar citation ID to ISM is not verified. Confirm the title before merging.
2. **Career dates:** The repository and June CV list Microsoft as May 2026 to Present, MS as 2021–2023, and PhD as 2023–Present. These dates were retained; confirm whether the internship has ended and whether the degree dates are correct.
3. **Existing metrics:** Pre-existing statements such as 85% transfer success, 20% sample efficiency gain, and 60,000 PyPI downloads were not independently audited. The credit-card project emphasizes accuracy on imbalanced data; precision/recall or PR-AUC would substantiate its value better if available.
4. **Contact delivery:** The existing Formspree endpoint was preserved. No message was submitted, so delivery remains untested.
5. **Venue claims:** IGARSS acceptance was retained from the original site, not newly inferred from arXiv. The Emergence blog stays clearly labeled as a blog.

## Validation scope

Eight HTML routes and their local references, anchors, navigation, image alt attributes, and CSS asset paths were checked offline. JavaScript syntax and menu state transitions were checked. The generated CV was rendered and visually inspected. Browser viewport testing and external form delivery were not performed. These changes are prepared for review, not merged or deployed.
