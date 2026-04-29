'''
Assignment 1 submitted by Saachi Varma Y

* Takes marks as input from the user using a loop
* Uses conditional statements to evaluate and display the result (for example: pass/fail, grades, etc.)
'''

def grades(marks):

    for subject, score in marks.items():

        print(subject + " : " + str(score))

        if score >= 35:
            print("PASS")
            if score >= 90:
                print("Grade: A")
            elif score >= 75:
                print("Grade: B")
            elif score >= 60:
                print("Grade: C")
            else:
                print("Grade: D")

        else:
            print("FAIL")
            print("Grade: F")
              

if __name__ == "__main__":

    num = int(input("enter no. of subjects: "))
    marks = {}

    for i in range(num):

        subject = input("Name of subject "+str(i+1)+": ")
        score = int(input("Enter marks in "+subject+": "))

        marks[subject] = score

        
    grades(marks)

    total_marks = 0
    for score in marks.values():
        total_marks +=score
        
    percentage = (total_marks/(num*100))*100
    print("Total percentage = "+str(percentage))

    


