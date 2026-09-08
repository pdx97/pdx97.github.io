"""Build the public CV from the website's current content.
Dependencies: beautifulsoup4, reportlab. Run sync_ism.py first.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("CVSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("CVSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("CVSans", normal="CVSans", bold="CVSans-Bold", italic="CVSans", boldItalic="CVSans-Bold")
ROOT=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='CVSans-Bold',fontSize=27,leading=31,textColor=HexColor('#173e42'),spaceAfter=8))
styles.add(ParagraphStyle(name='SectionCV',fontName='CVSans-Bold',fontSize=14,leading=18,textColor=HexColor('#173e42'),spaceBefore=14,spaceAfter=10,keepWithNext=True))
styles.add(ParagraphStyle(name='TitleCV',fontName='CVSans-Bold',fontSize=9.5,leading=12,spaceBefore=5,spaceAfter=2,keepWithNext=True))
styles.add(ParagraphStyle(name='TextCV',fontName='CVSans',fontSize=8.8,leading=11.5,spaceAfter=4))
styles.add(ParagraphStyle(name='MetaCV',fontName='CVSans',fontSize=8.2,leading=10,textColor=HexColor('#40575b'),spaceAfter=2))
styles.add(ParagraphStyle(name='BulletCV',fontName='CVSans',fontSize=8.8,leading=11.5,leftIndent=10,firstLineIndent=-7,spaceAfter=2))
def clean(t):
 return ' '.join(t.split()).replace('—','-').replace('–','-').replace('→','to').replace('🥇','').replace('’',"'")
def txt(node): return escape(clean(node.get_text(' ',strip=True))) if node else ''
def soup(name):return BeautifulSoup((ROOT/(name+'.html')).read_text(),'html.parser')
def para(t,style='TextCV'):return Paragraph(t,styles[style])
def section(t):story.append(para(t,'SectionCV'))
def link(a):return '<a color="#176776" href="'+escape(a['href'],quote=True)+'">'+txt(a)+'</a>'
story=[]
story.append(para('Prakhar Dixit','NameCV'))
story.append(para('PhD Student in Computer Science | University of Maryland, Baltimore County','TitleCV'))
story.append(para('Baltimore, Maryland | <a href="mailto:prakhhar1997@gmail.com">prakhhar1997@gmail.com</a> | +1 202 937 5716','MetaCV'))
story.append(para('<a href="https://pdx97.github.io/">Website</a> | <a href="https://scholar.google.com/citations?user=oa-29J8AAAAJ">Google Scholar</a> | <a href="https://www.linkedin.com/in/prakhardixit250697/">LinkedIn</a> | <a href="https://github.com/pdx97">GitHub</a>','MetaCV'))
story.append(para(txt(soup('index').select_one('.hero-bio'))))
section('Publications & Technical Writing')
for card in soup('publications').select('.pub-item'):
 block=[para(txt(card.select_one('.pub-title')),'TitleCV'),para(txt(card.select_one('.pub-authors')),'MetaCV'),para(txt(card.select_one('.pub-venue'))+' | '+txt(card.select_one('.pub-year')),'MetaCV'),para(' | '.join(link(a) for a in card.select('.pub-links a')),'MetaCV')]
 story.append(KeepTogether(block))
story.append(PageBreak())
section('Research & Professional Experience')
for card in soup('experience').select('.tl-card'):
 story.extend([para(txt(card.h3),'TitleCV'),para(txt(card.select_one('.meta')),'MetaCV')])
 for li in card.select('li'):story.append(para('- '+txt(li),'BulletCV'))
 story.append(Spacer(1,5))
story.append(PageBreak())
section('Education')
for card in reversed(soup('education').select('.stair')):
 story.extend([para(txt(card.select_one('.stair-degree'))+' | '+txt(card.select_one('.stair-school')),'TitleCV'),para(txt(card.select_one('.stair-dates'))+' | '+txt(card.select_one('.stair-gpa')),'MetaCV'),para(txt(card.select_one('.stair-note')))])
section('Projects')
for card in soup('projects').select('.project-card'):
 story.append(KeepTogether([para(txt(card.h3),'TitleCV'),para(txt(card.p)),para(' | '.join(link(a) for a in card.select('.project-links a')),'MetaCV')]))
story.append(PageBreak())
section('Technical Skills')
for card in soup('education').select('.skill-group'):
 story.append(para('<b>'+txt(card.h3)+':</b> '+', '.join(txt(t) for t in card.select('.skill-tag'))))
section('Presentations & Honors')
for card in soup('honors').select('.honor-item'):
 story.append(KeepTogether([para(txt(card.select_one('.honor-title')),'TitleCV'),para(txt(card.select_one('.honor-meta')),'MetaCV')]))
section('Academic Service')
for item in soup('publications').select('.review-item'):story.append(para('- '+txt(item),'BulletCV'))
def footer(c,doc):
 c.setStrokeColor(HexColor('#ccd7d9'));c.line(45,39,567,39);c.setFont('CVSans',8);c.setFillColor(HexColor('#40575b'));c.drawString(45,26,'Prakhar Dixit | CV updated September 2026');c.drawRightString(567,26,str(doc.page))
doc=SimpleDocTemplate(str(ROOT/'Docs/Prakhar_Dixit_CV.pdf'),pagesize=(612,792),rightMargin=45,leftMargin=45,topMargin=37,bottomMargin=53,title='Prakhar Dixit - Curriculum Vitae',author='Prakhar Dixit')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Created Docs/Prakhar_Dixit_CV.pdf')
