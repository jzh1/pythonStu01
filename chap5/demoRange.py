# rage(stop),rage(start,stop),rage(start,stop,step)
# rage(开始,结束,'步长')
# 不用是不生成这个序列的，所以占用的内存相同；当使用的时候才会真正产生
r = range(10)
r1 = range(3, 9)
r2 = range(3, 30, 2)

print(list(r))
print(list(r1))
print(list(r2))
# 判断是否在当前序列
print(10 in list(r2))
print(10 not in list(r2))
