num = input("Enter a number:\n")
number = int(num)


def factorial(digit):
    if digit == 0 or digit == 1:
        return 1
    elif digit < 0:
        return "Use a positive number"
    else:
        while digit >=1:
            fact = digit * factorial(digit - 1)
            return fact

print("The factorial of "+num+" is "+ str(factorial(number)))