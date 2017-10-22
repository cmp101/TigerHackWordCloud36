# import newspaper
from newspaper import Article

# news_paper=newspaper.build(u'http://www.npr.org/sections/news/')
# print(news_paper.size())
# for article in news_paper.articles:
	# print(article.url)

 # url1 = 'http://www.npr.org/2017/10/13/556664338/trump-to-put-iran-nuclear-deal-in-limbo-by-refusing-to-certify'
url= 'http://www.bbc.com/news/world-africa-41621660'
a = Article(url) 

a.download()
a.parse()

print(a.text[:].encode('utf-8').strip())
