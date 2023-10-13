# tkinter: 內建
# pyQT: py轉接頭要錢
import tkinter as tk
# MAC
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
req.urlretrieve(url, "dict.big")

# 1. 分詞
# 先用詞典作初步的猜測 -> (運用機率算法)決定哪個機率最高
import jieba
import jieba.analyse
jieba.set_dictionary("dict.big")
# jieba.load_userdict("mydict.txt")


# 元件(父元件)
# 元件.排版
# pack: 上下左右
# grid: 表格型
# Entry(單行) Text(多行) Label Button
def analyse():
    global t1, result
    s = t1.get("1.0", "end")
    keywords = jieba.analyse.extract_tags(s, topK=5)
    show = "/".join(keywords)
    result["text"] = show


window = tk.Tk()
window.geometry("500x500+250+250")
f1 = tk.Frame(window)
f1.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)
l1 = tk.Label(f1, text="請輸入文章")
l1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
t1 = tk.Text(f1)
t1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
b1 = tk.Button(f1, text="請按我", command=analyse)
b1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
result = tk.Label(f1, text="分析結果")
result.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
tk.mainloop()