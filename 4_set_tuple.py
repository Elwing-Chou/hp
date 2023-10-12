# set: 不重複集合
# no key
names = {"周", "王", "周", "黃"}
print(names)

print(names & {"周"})
print(names | {"何", "王"})
print(names - {"周"})

# 查找快速的集合
# [30, 20, 60, 50] -> 找某個東西最慘走完list
# set不用, 因為set的每個東西都會做出一個hash直 先比對hash直, 才再作進一步比較
# 可以hash東西: Immutable(不可變)
# Immutable: 數字/字串/tuple
# Mutable: list, dict, set
# XXXXX: {[1, 2]} set裡放list不行

# tuple: 簡化版的字典, immutable
# key: 0, 1, 2
t = (255, 255, 255)
points = {(0, 1), (2, 3)}
print(points)
counts = {
    (0, 1):5,
    (2, 3):10
}
print(counts)