# fixed arguments
def display(a, b, c):
    c = a + b
    return c

total = display(1, 2, 3)
print(total)

# default
def display2(a=0, b=0):
    print("This is for display2 =", a, b)

display2()
display2(10)
display2(10, 20)