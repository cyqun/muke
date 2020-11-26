# coding: utf-8

# 定义变量service_menu用来存储服务类型
service_menu = {1: "人民币转换美元", 2: "美元转换人民币", 3: "人民币转换欧元", 0: "结束程序"}

while True:
    print('**********欢迎使用货币转换系统**********')
    # 输出四种数据
    for i, j in service_menu.items():
        print('{0}.{1}'.format(i, j))

    # 输入服务类型
    Your_Choice = int(input("请您选择需要的服务："))

    # 人民币转美元
    if Your_Choice == 1:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("欢迎使用人民币转换美元服务")
        # 需要转换的金额并输出
        your_money = int(input("请输入需要转换的人民币金额："))
        print("您需要转换的人民币为：", your_money, end='')
        print("元")
        # 汇率换算
        RMB_to_US = your_money / 7.06
        # 输出转换后的结果并保存小数点后两位
        print("兑换成美元为：{:0.2f}".format(RMB_to_US), end="")
        print("$")
        print('==================================')

    # 美元兑换人民币
    elif Your_Choice == 2:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("欢迎使用美元兑换人民币服务")
        your_money = int(input("请输入需要转换的美元金额："))
        print("您需要转换的美元为：", your_money, end="")
        print("$")
        US_to_RMB = your_money * 7.06
        print("兑换成人民币为：{:0.2f}".format(US_to_RMB), end="")
        print("元")
        print('==================================')

    # 人民币转换欧元
    elif Your_Choice == 3:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("欢迎使用人民币转换欧元服务")
        your_money = int(input("请输入需要转换的人民币金额："))
        print("您需要转换的人民币为：", your_money, end='')
        print("元")
        RMB_to_EUR = your_money * 0.12
        print("兑换成欧元为：{:0.2f}".format(RMB_to_EUR), end="")
        print("€")
        print('==================================')

    # 当输入位0时，结束程序，跳出循环
    elif Your_Choice == 0:
        print('感谢你的使用,祝你生活愉快,再见!')
        print('==================================')
        break
    # 输入的值非0,1,2,3时，给予提示
    else:
        print("您输入有误！请按照提示输入0,1,2,3，谢谢！")


