numbers = []
def uuu(i):
    if i < i + 1:
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottle i is {i}")
        uuu(i+1)
uuu(1)
#哇 达哥哥真厉害！