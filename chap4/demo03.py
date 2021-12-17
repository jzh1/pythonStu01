# 选择结构 if else
money = 11.1

# 单分支
getMoney = int(input('请输入取款金额：'))
if getMoney <= money:
    money = money-getMoney
    print("取款成功，余额：", money)

