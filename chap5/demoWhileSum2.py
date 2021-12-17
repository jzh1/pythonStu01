# 循环结构
a = 0
# 偶数和
sum1 = 0
# 奇数和
sum2 = 0
while a < 100:
    # print(a)
    if a % 2 == 0:
        sum1 += a
    else:
        sum2 += a
    a += 1

print('偶数和为：' + str(sum1) + "，奇数和为：" + str(sum2))
