import sys
from os import system, name
from time import sleep


def cp():
    print(
    """
                Global AI Hub  
            Introduction to Python 
          Homework IV — Ugurcan Dede
    """)

system("cls")
cp()
print("\n\n**************\nSet a Default User\n**************\n")
def_name = input("Set Default Name\n")
def_sur = input("Set Default SurName\n")
print("\n\n**************\nDefault User Setted\n**************\n\n")
sleep(2)
system("cls")


class lesson:
    lessons = ["python", "javascript", "java", "big data"]

    def __init__(self):
        self.grades = {"mterm": 0, "fnl": 0, "prj": 0}
        self.selectLesson()

    def selectLesson(self):
        print(self.lessons)
        answ = input("Do you want to add a lesson? (y/n) ")
        self.addLesson(answ)

        lessonCount = int(input("How many lessons will you take "))
        self.calculateNumberLessons(lessonCount)

    def addLesson(self, answ):
        while answ != "n":
            lName = input("Lesson name to add: ")
            self.lessons.append(lName.lower())
            print("All Lessons\n", self.lessons)
            answ = input("Do you want to add a lesson? (y/n) ")

    def calculateGrade(self):
        grade = (self.grades["mterm"] * 0.3)+(self.grades["fnl"] * 0.5)+(self.grades["prj"] * 0.2)
        if grade > 90:
            print("AA\tYou passed.")
        elif grade <= 90 and grade > 70:
            print("BB\tYou passed.")
        elif grade <= 70 and grade > 50:
            print("CC\tYou passed.")
        elif grade <= 50 and grade >= 30:
            print("DD\tYou passed.")
        else:
            print("FF\tYou failed.")

    def saveNote(self, m, f, p):
        self.grades["mterm"] = m
        self.grades["fnl"] = f
        self.grades["prj"] = p

    def calculateNumberLessons(self, count):
        if count < 3 or count > 5:
            print("You can take maximum 3, minimum 5 lesson")
        else:
            print("\nAvailable lessons\n", self.lessons)
            for _ in range(count):
                lesson = input("\nPlease choose a lesson: ")
                if lesson in self.lessons:
                    v = int(input("{} mid-term exam grade: ".format(lesson).capitalize()))
                    f = int(input("{} final exam grade: ".format(lesson).capitalize()))
                    p = int(input("{} project grade: ".format(lesson).capitalize()))
                    
                    self.saveNote(v, f, p)
                    self.calculateGrade()
                else:
                    print("\nThe value you entered was not found\n")


class student:
    name = ""
    surname = ""

    def __init__(self, name, surname):
        system("cls")
        cp()
        self.name = name
        self.surname = surname
        for t in range(3):
            if self.name == def_name and self.surname == def_sur:
                system("cls")
                cp()
                print("\n\t\tWelcome {} {}\n".format(self.name, self.surname))
                break
            elif t == 2:
                print("Too many Wrong system closed")
                sys.exit()
            else:
                print("\nPlease Check infos\n")
                self.name = input("Please enter name\n")
                self.surname = input("Please enter surname\n")


def main():
    cp()
    try:
        name = input("Please enter name\n")
        sname = input("Please enter surname\n")
        student(name, sname)
        lesson()
    except:
        print("\n\nAn Error Has Occurred\n\n".upper())
    


if __name__ == "__main__":
    main()
