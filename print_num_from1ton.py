#query:print 1 to n 

n = int(input("enter a value: "))

i = 1

while i <= n:
    print(i)

    i+=1


for i in range(1,n+1):
    print(i)

#print sum of natural numbers 1 to n
i = 1
sum = 0
while i <= n:
    sum = i + sum
    i+=1
print(sum)

#print even numbers fron 1 to n

i = 1

while i<=n:
    if i%2 == 0:
        print(i)

    i+=1



#using continue print even numbers

i=1

while i<=n:
    if not (i%2 == 0):
        i+=1

        continue


    print(i)
    i+=1

print(len("python"))



