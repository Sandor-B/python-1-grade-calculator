AmountOfLabs = int(input("Enter the number of labs completed: "))
AmountOfQuizzes = int(input("Enter the number of quizzes completed: "))

Assignment1 = int(input("Enter the grade for Assignment 1: "))
Assignment2 = int(input("Enter the grade for Assignment 2: "))
Assignment3 = int(input("Enter the grade for Assignment 3: "))
Assignment4 = int(input("Enter the grade for Assignment 4: "))

Midterm1 = int(input("Enter the grade for Midterm 1: "))
Midterm2 = int(input("Enter the grade for Midterm 2: "))

FinalExam = int(input("Enter grade for Final Exam: "))

FinalMidtermPreparations = int(input("Enter grade for Midterms and Final Preparation: "))

if AmountOfLabs > 5: AmountOfLabs = 5
if AmountOfQuizzes > 5: AmountOfQuizzes = 5

StudentGrade = (AmountOfLabs * 4) + (AmountOfQuizzes * 3) + (Assignment1 * 0.04) + (Assignment2 * 0.04) + (Assignment3 * 0.04) + (Assignment4 * 0.04) + (Midterm1 * 0.125) + (Midterm2 * 0.125) + (FinalExam * 0.18) + (FinalMidtermPreparations * 0.06)

StudentGrade = str(round(StudentGrade, 2))

print("Your grade is: " + StudentGrade)
