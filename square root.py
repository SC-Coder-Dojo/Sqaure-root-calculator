from math import sqrt
print('Type in a number to find the square root of it!')
x = input()
x = float(x)

if x < 0:
    print("You can't sqaure root a negitive number.")
    print("Open the file again after pressing enter.")
    input()
else:
    print(sqrt(x))
    input()
