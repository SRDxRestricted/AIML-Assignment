num_subjects=int(input("Enter number of subjects"))
total=0;
for i in range(num_subjects):
    marks=int(input(f"Enter Marks for Each Subject {i+1}:"))
    total+=marks
avg=total/num_subjects
print("Average Marks:",avg)
if avg>=90:
    print("Grade:A")
elif avg>=75:
    print("Grade:B")
elif avg>=50:
    print("Grade C")
else:
    print("Fail")