many_people_on_the_bus = "Tom Bob Mary James Curry"
first_bus = many_people_on_the_bus.split(' ')
print("people= ",first_bus)
second_bus =["Zed", "Sky","Green"]
while len(first_bus) != 8:
    减少的人 = second_bus.pop()
    print("Adding = ",减少的人)
    first_bus.append(减少的人)
    print(first_bus)

print("second_bus has: ",second_bus)

print(first_bus[1] )