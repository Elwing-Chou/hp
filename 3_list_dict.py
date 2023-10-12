# 四種群集型態
# list/set/dict/tuple
# list(清單)

# key->value: 查詢操作  群集[key]
# python偷給的: 0 1 2
#             -3 -2 -1
scores = [30, 20, 80, 50, 60]
print(scores)

print(scores[0])
print(len(scores), max(scores), sum(scores))
print(30 in scores)

# print(scores[len(scores)-1])
print(scores[-1])

count = 0
for s in scores:
    if s >= 60:
        count = count + 1
print(count)

# dict: 組合多個東西來表示一個複雜東西
# [學生, 學生...]
# 自訂key(數字, 字串...)
student = {
    "姓名":"Elwing",
    "身高":175
}
print(student["身高"])
student["體重"] = 85
print(student)

# JSON格式: [], {}
exhibitions = [
    {
        "名稱":"Python特展",
        "地點":[0, 1]
    },
    {
        "名稱":"恐龍特展",
        "地點":[1, 2]
    }
]
# w: 寫入 r: 讀取
# win預設編碼: ANSI(X) unix: utf-8
import json
f = open("ex.json", "w", encoding="utf-8")
json.dump(exhibitions,
          f,
          ensure_ascii=False,
          indent=4)
# 專屬功能(method)
f.close()







