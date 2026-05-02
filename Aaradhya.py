n = int(input("Enter no. of subjects:"))
total = 0

for i in range(n):
    marks = int(input("enter your marks:"))
    total += marks
    
    if marks >=90:
        grade = "A++"
    elif marks >= 80:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    if marks >= 40:
        result = " yoo Passs"
    else:
        result = "Fail!"

print("Marks:", marks)
print("Result:", result)
print("Grade:", grade)