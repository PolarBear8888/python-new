print("""走过路过， 瞧一瞧， 看一看了啊!~
刚孵化的幼龙你要哪一只啊？绝对刚孵化的，假一赔十！
您要火龙(珈珈) 还是 水龙(铭铭)""")

dragon = input(">>> ")

if dragon == "火龙"or "珈珈":
    print("""Wo, 既然选择了，就来点食物喂它吧！
有 芒果 草莓 和 西瓜， 你要哪个呢？""")
    
    fruit = input(">>> ")
    
    if fruit == "西瓜":
        print("你看， 它变成绿色了！")

    elif fruit == "芒果":
        print("快给它吃点感冒药， 他快热死了！")
    
    elif fruit == "草莓":
        print("一副享受的样子，看来，它最喜欢吃的是草莓！")
    
    else:
        print(f"很可惜，{fruit}卖完了，下次早点来噢！")

elif dragon == "水龙" or "铭铭":
    print("""Wo, 既然选择了，就来点食物喂它吧！
有 苹果 榴莲 和 猕猴桃， 你要哪个呢？""")
     
    fruit2 = input(">>> ")
    
    if fruit2 == "苹果":
        print("看它的样子， 苹果不是它喜欢吃的！")

    elif fruit2 == "榴莲":
        print("虽然，它喜欢吃榴莲，但是，榴莲太贵了，下次试试猕猴桃吧")

    elif fruit2 == "猕猴桃":
       print("猕猴桃是铭铭最喜欢吃的食物，一天能吃一车！")
    else:
        print(f"很可惜，{fruit}卖完了，下次早点来噢！")

else:
    print("很抱歉，其他的卖光了，明天再来吧！")