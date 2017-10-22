#!/usr/bin/env python
# coding=utf-8
from wordcloud import WordCloud
from PIL import Image
import numpy as np

#alice_mask = np.array(Image.open("./other/alice_mask.png"))
text1 = open('./temp.txt').read()
text2 = open('./model/fil9_head.txt').read()
text = text1+text2
wordcloud = WordCloud(width=1500,height=700,max_words=3000,stopwords="").generate(text)
image = wordcloud.to_image()
image.save("./temp/output/output.png",format='png')
