import os
import newspaper
import argparse
import sys
import os.path
from datetime import datetime
from newspaper import Article



save_path = sys.argv[1]
numberofarticle = int(sys.argv[2])
# print(numberofarticle)

# news_paper=newspaper.build(u'http://www.ky3.com/news/')
# news_paper=newspaper.build(u'https://www.usatoday.com/')
# print(news_paper.size())
# for article in news_paper.articles:
	# file=open("usatoday.txt","w")
	# file.write(article.url)
	# print(article.url)
module_path = os.path.dirname(__file__)
file = open(module_path + "/ky3.txt","r")
content=file.read()
# print(content)
newlist = content.splitlines()
number = numberofarticle-1;

for x in range(0,number):
    
	filename=('{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S')))
	newfilename= "news"+str(number)+filename
	completename=os.path.join(save_path,newfilename)
	f = open(completename,"w")
	
	temp=newlist[x]
	url= temp
	a = Article(url) 
	a.download()
	a.parse()
	f.write(a.text[:].encode('utf-8').strip())
	

	

# url= 'https://www.columbiamissourian.com/news/local/benefit-planned-to-help-young-girl-recovering-from-brain-tumor/article_a02230b8-af7f-11e7-8995-8fb45b1b246b.html'
# a = Article(url) 

# a.download()
# a.parse()

# print(a.text[:].encode('utf-8').strip())
