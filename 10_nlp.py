# MAC
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
req.urlretrieve(url, "dict.big")

# 1. 分詞
# 先用詞典作初步的猜測 -> (運用機率算法)決定哪個機率最高
import jieba
jieba.set_dictionary("dict.big")
jieba.load_userdict("mydict.txt")

f = open("news.txt", "r", encoding="utf-8")
s = f.read()
f.close()
# print(s)

print(" ".join(jieba.cut(s)))

# 2. 抓出關鍵詞
# 次數: 高, 關鍵程度越高
# 常用度: 低, 關鍵程度越高
# tfidf = 次數(tf) * 1/常用度(idf)
import jieba.analyse
keywords = jieba.analyse.extract_tags(s)
print(keywords)
keywords = jieba.analyse.extract_tags(s, allowPOS=["nr", "ns", "nt"])
print(keywords)