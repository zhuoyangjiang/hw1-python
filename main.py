# Author: zhuoyangjiang zfj5038@psu.edu

def getGradePoint(grade):
    if grade == "A":
        return 4.0
    elif grade == "A-":
        return 3.67
    elif grade == "B+":
        return 3.33
    elif grade == "B":
        return 3.0
    elif grade == "B-":
        return 2.67
    elif grade == "C+":
        return 2.33
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    else:
        return 0.00

def run():
    gradepoint1 = getGradePoint(input("Enter your course 1 letter grade: "))
    credit1 = int(input("Enter your course 1 credit:"))
    print(f"Grade point for course 1 is: {gradepoint1}")

    gradepoint2 = getGradePoint(input("Enter your course 2 letter grade: "))
    credit2 = int(input("Enter your course 2 credit:"))
    print(f"Grade point for course 2 is: {gradepoint2}")

    gradepoint3 = getGradePoint(input("Enter your course 3 letter grade: "))
    credit3 = int(input("Enter your course 3 credit:"))
    print(f"Grade point for course 3 is: {gradepoint3}")

    GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
    print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
    run()