a = int(input("Enter the marks in english : "))
b = int(input("Enter the marks in telugu : "))
c = int(input("Enter the marks in maths : "))

total_marks = a+b+c
average = total_marks/3

grade = ""

if average > 90:
    grade = "A"
if average > 80 and average<90:
    grade = "B"
if average > 70 and average<80:
    grade = "C"



print(f"Total marks:{total_marks}\nAverage marks:{average}\nGrade:{grade} ")


