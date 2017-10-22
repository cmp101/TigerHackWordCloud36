#!/usr/bin/env python
# coding=utf-8
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import re
import os
import sys

p = re.compile(r' ')

a = {'control': 6, 'week': 4, 'love': 1, 'ad': 9, 'deal': 3, 'people': 11, 'breakout': 3, 'intelligence': 3, 'dead': 4, 'production': 6, 'sea': 4, 'crash': 17, 'trump': 21, 'lie': 9, 'death': 4, 'injure': 4, 'travel': 3, 'airport': 3, 'ice': 10, 'militant': 8, 'virgin': 6, 'program': 1, 'cooperation': 2, 'treasury': 2, 'employee': 19, 'gate': 3, 'care': 10, 'stock': 5, 'musk': 6, 'model': 9, 'ivory': 4, 'flight': 16, 'rescue': 2, 'business': 8, 'fire': 13, 'chancellor': 15, 'company': 16, 'income': 18, 'water': 6, 'plane': 5, 'china': 9, 'president': 14, 'law': 6, 'marine': 6, 'payment': 6, 'change': 9, 'penguin': 12, 'steel': 5, 'island': 13, 'official': 7, 'benefit': 10, 'airline': 4, 'social': 21, 'military': 3, 'security': 21, 'support': 3, 'wind': 4}


#alice_mask = np.array(Image.open("./other/alice_mask.png"))
#for line in sys.stdin:
#    a[(p.split(line)[1].strip('\n'))] = int(p.split(line)[0]);

#print a



#text2 = open('./model/fil9_head.txt').read()
#text = text1+text2
wordcloud = WordCloud(width=1500,height=800).generate_from_frequencies(a)
image = wordcloud.to_image()
image.save("./temp/output/output.png",format='png')
