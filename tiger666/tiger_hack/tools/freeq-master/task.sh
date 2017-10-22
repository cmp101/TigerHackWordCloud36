python freeq.py
python filter.py
python merge.py
cat wordsFreOfAllNews.txt | python ../../rel.py > 999.txt && cat 999.txt | ../../tools/fasttext nn ../../model/fil9.bin >> 1.txt 
rm -rf 999.txt
rm -rf 1.txt
python removeSynonym.py

