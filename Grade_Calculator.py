AmountOfLabs = int(input("\nEnter the number of labs completed: "))
AmountOfQuizzes = int(input("Enter the number of quizzes completed: "))

Assignment1 = float(input("Enter the grade for Assignment 1: "))
Assignment2 = float(input("Enter the grade for Assignment 2: "))
Assignment3 = float(input("Enter the grade for Assignment 3: "))
Assignment4 = float(input("Enter the grade for Assignment 4: "))

Midterm1 = float(input("Enter the grade for Midterm 1: "))
Midterm2 = float(input("Enter the grade for Midterm 2: "))

FinalExam = float(input("Enter grade for Final Exam: "))

FinalMidtermPreparations = float(input("Enter grade for Midterms and Final Preparation: "))

if AmountOfLabs > 6: AmountOfLabs = 6
if AmountOfQuizzes > 6: AmountOfQuizzes = 6

StudentGrade = (AmountOfLabs * 3.333) + (AmountOfQuizzes * 2.5) + (Assignment1 * 0.04) + (Assignment2 * 0.04) + (Assignment3 * 0.04) + (Assignment4 * 0.04) + (Midterm1 * 0.125) + (Midterm2 * 0.125) + (FinalExam * 0.18) + (FinalMidtermPreparations * 0.06)

StudentGrade = str(round(StudentGrade, 2))

print("Your grade is: " + StudentGrade)
