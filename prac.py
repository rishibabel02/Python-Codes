# class ChangeList(object):
#     def __init__(self , any_list):
#         self.any_list = any_list
#     def do_add(self):
#         self.sum = sum(self.any_list)
#         print(create_sum.sum)

# my_list = [1,2,1,4,5]
# create_sum = ChangeList(my_list)
# create_sum.do_add()

# class Person:
#     def __init__(self , name):
#         self.name = name
#     def say (self):
#         print("Hello , my name is ",self.name)

# p = Person("Rishi")
# p.say()

# class students():
#     def __init__(self, name , contact):
#         self.name =name
#         self.contact = contact

#     def getdata(self):
#         print("Enter student data:")
#         self.name = input("Enter name of student ")
#         self.contact = input("Enter contact number ")

#     def printdata(self):
#         print("Student Information ")
#         print("\n Name :"+self.name , "\n Contact:"+self.contact)

# class engg(students):
#     def __init__(self, age):
#         self.age = age

#     def input(self):
#         print("Age:")
#         self.age = int(input("Enter age of the student "))

#     def display(self):
#         print("Age is :",self.age)

# abc = engg(20)
# abc.getdata()  #inherited class can use methods of the base class
# abc.printdata()
# abc.input()
# abc.display()



