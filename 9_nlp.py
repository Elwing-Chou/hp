# 1. 分詞
# 先用詞典作初步的猜測 -> (運用機率算法)決定哪個機率最高
import jieba
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