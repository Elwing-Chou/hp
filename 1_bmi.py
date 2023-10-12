# bmi: weight(kg) / height(m) ^ 2
# =(是/取代) ==(相等)
# 數字(integer)(float) 字串(string)
# int() float() str()
weight = float(input("請輸入體重:"))
height = float(input("請輸入身高:"))
bmi = weight / (height / 100) ** 2
print("我的體重是:" + str(weight))
print("我的身高是:", height)
print("bmi是:", bmi)

# 如果...否則如果...否則
# 縮排(:/TAB)
if bmi > 25:
    print("過重")
    print("你要多運動")
elif bmi > 18:
    print("正常")
else:
    print("過輕")
print("!!!!!")
