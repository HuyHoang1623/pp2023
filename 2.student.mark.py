class Student:
    def __init__(self, studentID, name, dob):
        self.studentID = studentID
        self.name = name
        self.dob = dob

    def getStudentID(self):
        return self.studentID

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob


class Course:
    def __init__(self, courseID, name):
        self.courseID = courseID
        self.name = name

    def getCourseID(self):
        return self.courseID

    def getName(self):
        return self.name


class Mark:
    def __init__(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark


class School:
    def __init__(self):
        self.studentlist = {}
        self.courselist = {}
        self.marklist = {}

    def getStudentlist(self):
        return self.studentlist

    def getCourselist(self):
        return self.courselist

    def getMarklist(self):
        return self.marklist

    def inputStudent(self):
        nos = int(input("number of students:"))
        for i in range(nos):
            id = input("Student id:")
            name = input("Student name: ")
            dob = input("Student dob: ")
            self.studentlist[id] = Student(id, name, dob)

    def inputCourse(self):
        noc = int(input("number of courses:"))
        for i in range(noc):
            id = input("Course id:")
            name = input("Course name: ")
            self.courselist[id] = Course(id, name)

    def mark(self):
        courseID = input("course ID: ")
        if courseID not in self.courselist:
            return
        for studentID in self.studentlist:
            mark = float(input(f"Enter the mark for {self.studentlist[studentID].getName()}: "))
            if studentID not in self.marklist:
                self.marklist[studentID] = {}
            self.marklist[studentID][courseID] = mark

    def courseList(self, courseID):
        print(f"{courseID}: {self.courselist[courseID].getName()}")

    def studentList(self, studentID):
        print(f"{studentID}: {self.studentlist[studentID].getName()}")

    def Markforcourse(self):
        courseID = input("Enter the courseID: ")
        if courseID not in self.courselist:
            return
        for studentID in self.studentlist:
            if studentID in self.marklist and courseID in self.marklist[studentID]:
                print(f"{self.studentlist[studentID].getName()}: {self.marklist[studentID][courseID]}")
            else:
                print("choose again")

    def listcourse(self):
        for courseID in self.courselist:
            self.courseList(courseID)

    def liststudent(self):
        for studentID in self.studentlist:
            self.studentList(studentID)


school = School()
school.inputStudent()
school.inputCourse()

while True:
    print("Your option: ")
    print("1. Input marks for a course")
    print("2. Course list")
    print("3. Student list")
    print("4. Display mark for course ")
    print("5. Quit")
    selection = int(input("Enter your choice: "))
    if selection == 1:
        school.mark()
    elif selection == 2:
        school.listcourse()
    elif selection == 3:
        school.liststudent()
    elif selection == 4:
        school.Markforcourse()
    elif selection == 5:
        break
    else:
        print("choose again")

