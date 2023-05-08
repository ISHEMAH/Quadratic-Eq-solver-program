from math import*

name = input("Enter your name please: ")
print("Hello," + name + "\nThank you for using my program")
system  = input("From which of the following Coordinate system :\ncartesian,\npolar,\ncylindrical or\nspherical\n:")
to = input("Convert to: ")
def ctop():
if system == cartesian and to == polar:

    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    z = float(input("Enter the z coordinate: "))
    r = sqrt((x ^ 2) + (y ^ 2) + (z ^ 2))
    theta = tan(y / x)
    ctop():
elif system == polar:
    r = float(input("Enter the r coordinate: "))
    theta = float(input("Enter the theta angle: "))
