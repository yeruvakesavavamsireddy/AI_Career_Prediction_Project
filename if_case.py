b=4
a=6
print(a+b)
name="anjali devi "
print(len(name))

print(name.capitalize())
print(name.count(" "))
print(name.upper())
light= "green"
if light=="green":
    print("go")
elif light=="red":
    print("stop")
elif light=="yellow":
    print("look")
else:
    print("light broken")
for i in range(0,5):
    print(i)



a = input("Enter the Number: ")
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


