import os, fnmatch,re
os.rename('0.html','index.html')
arr=fnmatch.filter(os.listdir('.'),'*.html')
for i in arr:
	s=open(i,"r").read()
	if '<in' in s:
		f=re.search('<in (.*) in>',s).group(1)
		print(f)
		ff=open(f,"r").read()
		open(i,"w").write(s.replace('<in '+f+' in>',ff))