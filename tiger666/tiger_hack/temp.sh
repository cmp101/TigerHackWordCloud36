#!/bin/bash

cat ./tools/freeq-master/wordsFreOfAllNews.txt | python ./re1.py | ./tools/fasttext nn ./model/fil9.bin > ./tools/freeq-master/1.txt
python ./tools/freeq-master/removeSynonym.py

