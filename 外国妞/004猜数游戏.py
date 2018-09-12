import random
secret = random.randint(1,10)
print("________骚达达又来了______")
temp = input("请输入一个你所想到的数：")
guess = int(temp)
while guess != secret:
    if guess > secret:
            print("哥，大了大了~~~")
    else:
            print("嘿，小了！小了！")
    print("哎呀！猜错了，请重新输入吧：")
    temp = input("请输入一个你所想到的数：")
    guess = int(temp)
if guess ==secret:
        print("哼，猜对了也没有奖励")
        print("我草，你是小甲鱼肚子里面的蛔虫吗")
print("游戏结束，不玩了")
