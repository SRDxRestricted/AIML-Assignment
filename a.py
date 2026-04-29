total = 0
marksof_subjects = int(input("Enter number of subjects: "))

for i in range(marksof_subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total += marks

    if marks >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")


average = total / marksof_subjects
print("Average Marks =", average)


if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: D")