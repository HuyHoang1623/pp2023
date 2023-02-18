number_of_corse=int(input("press number of course:"));
for i in range (0,number_of_corse):
    idc = str(input("course ID:"))
    namec = str(input("course name"))
    number_of_students = int(input("press number of students:"));
    for i in range(0, number_of_students):
        ids = str(input("student ID:"))
        names = str(input("student name:"))
        DoB = str(input("student date of birth:"))
        mark = float(input("mark of this course:"))

List1 = [str(namec)]
List2 = [str(names)]
List3 = [str(namec),str(names),mark]
print(List1)
print(List2)
print(List3
