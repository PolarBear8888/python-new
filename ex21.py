def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age  = add(float(input()), 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
#35        74      180   50

# A puzzle for the extra credit, type it in angway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))
# 35+ (74 - (180* (50 / 2)) ) 
# 74+ (50-( 180/ 35))
print("That becomes: ", what, "Can you do it by hand?")