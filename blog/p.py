import os, fnmatch
from datetime import datetime
#python3 p.py && python3 ../p.py

post="<li><here></li>"
mp="<body><here></body>"
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
arr=fnmatch.filter(os.listdir('.'),'*.html')
xml='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><here></urlset>'
k=''
for i in arr:
	k=k+'<url>'+i+'</url><lastmod>'+datetime.today().strftime('%Y-%m-%d')+'</lastmod>'
mmm=xml.replace('<here>',k)
open('/home/a/Documents/seo/sitemap.xml','w').write(mmm)
tit=[]
for i in arr:
	tit.append(i.replace('.html',''))
m=list(chunks(tit,5))
for i in m:
	for i1 in i:
		m[m.index(i)][i.index(i1)]=post.replace("<here>",'<a href="https://p6l.github.io/blog/'+i1+'.html">'+i1+'</a>')
full=''
num=0
for i in m:
	for i1 in i:
		full=full+i1
	open('/home/a/Documents/seo/'+str(num)+'.html','w').write(mp.replace("<here>",full)+"<a href='"+str(num+1)+".html'>next</a>")
	full=''
	num=num+1
#tit