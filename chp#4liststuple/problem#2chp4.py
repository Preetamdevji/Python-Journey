student1 = int(input("enter your marks: "))
student2 = int(input("enter your marks: "))
student3 = int(input("enter your marks: "))
student4=  int(input("enter your marks: "))
student5 = int(input("enter your marks: "))
student6 = int(input("enter your marks: "))
student7 = int(input("enter your marks: "))

student_marks = [student1, student2, student3, student4, student5, student6, student7]
student_marks.pop(6)
student_marks.sort()
print(student_marks)