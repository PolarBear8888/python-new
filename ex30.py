people = 50
cars = 15 
trucks = 15


if cars > people:#这个情况输出
    print("We should take the cars.")
elif cars < people:#这个情况输出
    print("We should not take the cars.")
else:#其他情况输出
    print("We can't decide.")

if trucks > cars:#这个情况输出
    print("That's too many trucks.")
elif trucks < cars:#这个情况输出
    print("Maybe we could take the trucks.")
else:#其他情况输出
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars > people or trucks < cars:
    print("Ye!")
elif cars < people and trucks < cars:
    print("Yo!")
else:
    print("Nice!")
