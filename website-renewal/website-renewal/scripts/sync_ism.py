"""Render ISM references into committed HTML. Uses only Python's standard library."""
from pathlib import Path
from html import escape as e
import json,re
ROOT=Path(__file__).resolve().parents[1]
p=json.loads((ROOT/'data/ism.json').read_text())
title,authors,venue,date,summary=(e(p[k]) for k in ('title','authors','venue','date','summary'))
links=''.join(f'<a class="pub-link" href="{e(p[key],quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>' for key,label in [('paper','Paper'),('openreview','OpenReview'),('code','Code')])
card=f'''<article class="pub-item" id="ism"><img src="images/ICML_2026.png" alt="ICML" class="pub-logo" loading="lazy"><div class="pub-body"><div class="pub-meta"><span class="pub-venue">{venue}</span><span class="pub-year">{date}</span></div><h3 class="pub-title">{title}</h3><p class="pub-authors">{authors}</p><p class="pub-abstract">{summary}</p><div class="pub-links">{links}</div></div></article>'''
regions={
 'publication':card,
 'news':f'<div class="news-item"><span class="news-date">{date}</span><span class="news-text"><a href="publications.html#ism">{title}</a>, accepted to the <strong>AI4Math Workshop at ICML 2026</strong>.</span></div>',
 'project':f'<article class="project-card"><h3>{title}</h3><p>{summary}</p><div class="tags"><span class="tag">Mathematical reasoning</span><span class="tag">Agent memory</span></div><div class="project-links">{links}</div></article>',
 'experience':f'<li>Developed <a href="publications.html#ism">ISM</a>, a self-improving strategy memory for continual mathematical reasoning ({venue}).</li>',
 'education':'<a href="publications.html#ism">Related work: ISM</a>.'}
for path in ROOT.glob('*.html'):
 text=path.read_text()
 for name,html in regions.items():
  pattern=rf'(<!-- BEGIN ISM {name} -->).*?(<!-- END ISM {name} -->)'
  text=re.sub(pattern,lambda m:m[1]+'\n'+html+'\n'+m[2],text,flags=re.S)
 path.write_text(text)
print('Synchronized ISM across publications, homepage, projects, experience, and education.')
