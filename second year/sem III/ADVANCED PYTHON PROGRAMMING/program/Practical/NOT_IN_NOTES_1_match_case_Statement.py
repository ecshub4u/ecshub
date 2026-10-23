# Program: match case Statement
# Question: Write a program to demonstrate match...case statement. (Syllabus practical no. 9)

day = int(input("Enter day number (1-3): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

