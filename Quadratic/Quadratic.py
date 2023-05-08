import math

a = int(input('Enter the value of a :'))
b = int(input('Enter the value of b :'))
c = int(input('Enter the value of c :'))

check = input("Is your equation = (" + str(a) + "x^2) + (" + str(b) + "x)+ (" + str(c) + ")\n yes or no \n")


def solve(x, y, z):
    delta = (y ** 2) + (-4*x * z)
    x1 = ((-1 * y) + (math.sqrt(delta)))/(2 * x)
    x2 = ((-1 * y) - (math.sqrt(delta)))/(2 * x)
    print("X1 = " + str(x1) + " \n or \nX2 = " + str(x2))


if check == "yes":
    solve(a, b, c)
elif check == "no":
    a = int(input('Enter the value of a'))
    b = int(input('Enter the value of b'))
    c = int(input('Enter the value of c'))
else:
    print("Answer yes or no")
