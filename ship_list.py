

goods = [
            ['MacBookPro',10000],
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

for index,g in enumerate(goods):
    print(index,g[0],g[1])

for index,g in enumerate(goods):
    print(index,g[0],g[1])



for index, g in enumerate(goods):

    choice = input("购买：").strip()
    if choice.isdigit():
        print(goods[int(choice)][0])
        print(goods[int(choice)][1])

        good_price = int(goods[int(choice)][1])
        choice_good = goods[int(choice)][0]

        price = int(price) - int(good_price)

        if price >=0:

            ship.append(choice_good)

        else:
            print("余额不足，购物车先有：",ship,price)
            break



    else:
        print("请输入纯数字")
