# tkinter: 內建
# pyQT: py轉接頭要錢
import tkinter as tk

# 元件(父元件)
# 元件.排版
# pack: 上下左右
# grid: 表格型
# Entry(單行) Text(多行) Label Button
window = tk.Tk()
window.geometry("500x500+250+250")
f1 = tk.Frame(window)
f1.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)
l1 = tk.Label(f1, text="請輸入文章")
l1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
t1 = tk.Text(f1)
t1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
b1 = tk.Button(f1, text="請按我")
b1.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
result = tk.Label(f1, text="分析結果")
result.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
tk.mainloop()