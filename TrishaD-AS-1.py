# Input Marks from user using loop ; Evaluate Pass or Fail and Grades using conditional statements

marks=[]
s = int(input("Enter number of subjects :"))
for i in range(s):
    mark = float(input(f"Enter marks for subject {i+1} :"))
    marks.append(mark)
avg = sum(marks) / s
print(f"Average marks : {avg}")
if any(mark < 40 for mark in marks) :
    print("Result : Fail")
    print("Grade : F")
else :
    print("Result : Pass")
    if avg >=90:
        print("Grade : A+")
    elif avg>=80 :
        print("Grade : A")
    elif avg >=70:
        print("Grade : B")
    elif avg >=60:
        print("Grade : C")
    elif avg >=50:
        print("Grade : D")
    else :
        print("Grade : E")
