"""Offline checks for GitHub Pages routes, anchors, navigation and assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
import re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.main=0;self.active=[];self.nav=[];self.in_nav=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='nav':self.in_nav=True
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if tag=='img':assert 'alt' in a,'Image lacks alt text'
  if a.get('aria-current')=='page':self.active.append(a.get('href'))
  if self.in_nav and tag=='a' and a.get('href') not in self.nav:self.nav.append(a['href'])
  for key in ['src','href']:
   if key in a:self.links.append(a[key])
 def handle_endtag(self,tag):
  if tag=='nav':self.in_nav=False
pages={p.name:Page(p.read_text()) for p in ROOT.glob('*.html')}
expected={name for name in pages if name!='index2.html'}
count=0
for name,page in pages.items():
 assert page.h1==1 and page.main==1,(name,'Expected one h1 and main')
 assert all(n==1 for n in Counter(page.ids).values()),(name,'Duplicate ID')
 if name!='index2.html':
  assert set(page.nav)==expected,(name,'Navigation is inconsistent')
  assert page.active==[name],(name,'Incorrect current page')
 for url in page.links:
  u=urlsplit(url)
  if u.scheme or u.netloc:continue
  local=ROOT/unquote(u.path.lstrip('/')) if u.path else ROOT/name
  assert local.exists(),(name,'Missing target',url)
  if u.fragment and local.suffix=='.html':assert unquote(u.fragment) in pages[local.name].ids,(name,'Missing anchor',url)
  count+=1
for css in (ROOT/'assets/css').glob('*.css'):
 for raw in re.findall(r'url\(([^)]+)\)',css.read_text()):
  url=raw.strip('\"\' ');u=urlsplit(url)
  if not u.scheme and not u.netloc:assert (css.parent/unquote(u.path)).exists(),(css,url)
for name in ['index','publications','projects','experience','education']:
 assert 'ISM' in (ROOT/(name+'.html')).read_text(),name
print(f'PASS: {len(pages)} pages; {count} local references; navigation, anchors, image alt text, CSS assets, ISM coverage.')
