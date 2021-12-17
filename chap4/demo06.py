# 嵌套分支
answer = input('您是会员吗？y/n')
price = float(input('请输入您的消费金额：'))
if answer == 'y':
    # price = float(input('请输入您的消费金额：'))
    if price > 200:
        print("会员：打八折！")
    elif 100 < price < 200:
        print('会员：打九折')
    else:
        print('会员：打9.5折')
else:
    # price = float(input('请输入您的消费金额：'))
    if price > 200:
        print("非会员：打9.5折！")
    else:
        print('非会员：不打折')
