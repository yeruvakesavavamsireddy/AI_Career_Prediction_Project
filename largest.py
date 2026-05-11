a = input()

x,y,z = a.split(",")

num1 = int(x)
num2 = int(y)
num3 = int(z)

large = 0

if num1>num2:
    if num1>num3:
        large = num1
    else:
        large = num3

if num2>num3:
    if num2>num1:
        large = num2
    else:
        large = num1

if num3>num1:
    if num3>num2:
        large = num3
    else:
        large = num2

print(large)
