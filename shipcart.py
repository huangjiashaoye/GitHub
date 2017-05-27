#utf-8

Shiplist = [
            ['MacBookPro',15000],
            ['iphone',7800],
            ['mi',900],
            ['ipad',3400],
            ['联想',4500],
            ['戴尔',4000],
            ['大主宰',20]
            ]

price = input("请输入你的工资金额：")
print("你的工资为：",price)
ship = []


#for循环遍历出货品
for each in Shiplist:
    print(each[0],each[1])

    for each in Shiplist:
        price = int(price) - each[1]


        if int(price) >=0:

            ship.append(each[0])

        else:
            print("余额不足")
            print(ship)
        break



