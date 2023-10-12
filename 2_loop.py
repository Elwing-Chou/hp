# 計數器
# 初始化: i = 0
# 判斷: i < 5
# 增加: i = i + 1 (i++, i+=1)
i = 0
while i < 5:
    print(i + 1,
          5 - i,
          2 * i + 1)
    i = i + 1

# SOP 1. 走過一群東西
for c in "apple":
    print("!", c)

# SOP 2. 固定次數迴圈
# print(list(range(5)))
# print(list(range(2, 5)))
# print(list(range(2, 11, 3)))
for i in range(5):
    print(i+1)

total = 0
for i in range(5):
    total = total + (i + 1)
    print(total)

# SOP 3. 不固定次數的迴圈
# 四大基礎: 數字, 字串, 布林(True/False), 無(None)
# 布林: not(不) and(而且) or(或者)
import random

win, lose = 0, 0
while win < 3 and lose < 3:
    # -1: lose 0: even 1: win
    result = random.randint(-1, 1)
    print(result)
    if result == -1:
        lose = lose + 1
    elif result == 1:
        win = win + 1
if win > lose:
    print("WIN")
else:
    print("LOSE")

win, lose = 0, 0
while True:
    result = random.randint(-1, 1)
    print(result)
    if result == -1:
        lose = lose + 1
    elif result == 1:
        win = win + 1

    if win == 3:
        print("WIN")
        break
    elif lose == 3:
        print("LOSE")
        break

