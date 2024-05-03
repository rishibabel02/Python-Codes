class students():  # classs name

    def __init__(self,name,contact):  # init function ...by default parameter self,
        self.name=name
        self.contact=contact

    def getdata(self):   # function getdata by default parameter self,
       self.name = input(" Enter name of student ")
       self.contact= input(" Enter contact number ")

    def printdata(self):   # function printdata  by default parameter self
         print("\n Name of student is "+self.name, " \n Contact number is "+self.contact)

class engg(students):
    def __init__(self,age):
        self.age = age
    def input(self):
        self.age = input("Enter the age of students: ")

    def displ(self):
        print("Age is :", self.age)


raj  = engg(age=25)
raj.getdata()
raj.input()
raj.printdata()
raj.displ()