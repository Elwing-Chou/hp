# tkinter: 內建
# pyQT: py轉接頭要錢
import tkinter as tk
# MAC
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import time
import threading

import urllib.request as req
url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
req.urlretrieve(url, "dict.big")

# 1. 分詞
# 先用詞典作初步的猜測 -> (運用機率算法)決定哪個機率最高
import jieba
import jieba.analyse
jieba.set_dictionary("dict.big")
# jieba.load_userdict("mydict.txt")


class MyFrame(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.initcomponent()

    def initcomponent(self):
        self.l1 = tk.Label(self, text="請輸入文章")
        self.l1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.t1 = tk.Text(self)
        self.t1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.b1 = tk.Button(self, text="請按我", command=self.analyse)
        self.b1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.result = tk.Label(self, text="分析結果")
        self.result.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def analyse(self):
        def work():
            self.b1["state"] = tk.DISABLED
            time.sleep(5)
            s = self.t1.get("1.0", "end")
            keywords = jieba.analyse.extract_tags(s, topK=5)
            show = "/".join(keywords)
            self.result["text"] = show
            self.b1["state"] = tk.ACTIVE
        thread = threading.Thread(target=work)
        thread.start()

# 元件(父元件)
# 元件.排版
# pack: 上下左右
# grid: 表格型
# Entry(單行) Text(多行) Label Button


window = tk.Tk()
window.geometry("500x500+250+250")
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH)
f2 = MyFrame(window)
f2.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH)

tk.mainloop()