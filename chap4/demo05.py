# 多分支,多选一
score = int(input('请输入一个数值，判断评级：'))

if 100 <= score and score >= 90:
    print('A')
elif 89 >= score >= 70:
    print('B')
elif 69 >= score >= 60:
    print('C')
elif 59 >= score >= 0:
    print('D')
else:
    print('输入成绩不在有效范围内')
