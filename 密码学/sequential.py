# X^16+X^12+X^3++X+1
# 抽头位为10100 00000 01000 1
tap = [1, 1, 1, 0, 1,
       1, 1, 0, 1, 0,
       1, 0, 0, 0, 1, 1]  # 初始化队列
str = " ".join('%s' % id for id in tap)
print("原始的队列: ", str)
count = 0
flag = 1
while (flag):
    new = (tap[0]+tap[2]+tap[11]+tap[15]) % 2
    count += 1
    for i in range(len(tap)):
        tap[len(tap)-1-i] = tap[len(tap)-2-i]
    tap[0] = new
    str1 = " ".join('%s' % id for id in tap)  # 因为数组里是整形数，必须先转换类型
    print("第", count, "次移位: ", str1)
    if (str1 == str):
        print("周期是:  ", count)
        flag = 0
