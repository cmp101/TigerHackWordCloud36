import newspaper
from newspaper import Article
# print("Please Select from below:")
# print("1. Put a news paper source.")
# print("2. Use one default newspaper source. we use 'http://www.ky3.com/news/' as default")
# input = raw_input("")

	
url_input=raw_input("key in the url")
news_paper=newspaper.build(''+url_input)
print(news_paper.size())
for article in news_paper.articles:
	print(article.url)
	file=open("keyinurl.txt","w")
	file.write(article.url)