Student = []
Course = []
Mark = []


def student():
    nos = int(input("number of student:"))
    for i in range(nos):
        student_id = input("student id:")
        student_name = input("student name:")
        dob = input("student date of birth:")
        a = {"student id": student_id, "student name": student_name, "student date of birth": dob}
        Student.append(a)


def course():
    noc = int(input("number of course:"))
    for i in range(noc):
        course_id = input("course id:")
        course_name = input("course name:")
        b = {"course id": course_id, "course name": course_name}
        Course.append(b)


def input_mark(Course, Student):
    print(f"input marks for course (Course['course_name']")
    Course['mark'] = {}
    for a in Student:
        mark = input(f"-Student (Student['student_name']")
        Course['mark'][Student['id']] = mark


def list_student():
    print(Student)


def list_course():
    print(Course)


def show_mark(Course):
    for (student_id, mark) in Course['mark']:
        print(f"Student (student_id) has mark(mark)")


def main():
    student()
    course()
    print("list student")
    list_student()
    print("list course")
    list_course()
    input_mark()
    show_mark()

main()


