#Program to print grades
n = int(input("Enter number of subjects: "))
total = 0
for i in range(n):
    marks = int(input(f"Enter mark{i+1}: "))
    total += marks
avg= total / n
print("Average Marks:", avg)
if avg >= 90:
    print("Grade: A")
elif avg>= 75:
    print("Grade: B")
elif avg >= 50:
    print("Grade: C")
else:
    print("Grade: F")

#program to print Pass/Fail
n = int(input("Enter number of subjects: "))
total = 0
for i in range(n):
    marks = int(input(f"Enter mark{i+1}: "))
    total += marks
avg= total / n
if avg<=0 and avg>100:
	print("Invalid marks")
elif avg>=35 and avg<=100:
	print("Result : PASS")
else:
	print("Result : FAIL")