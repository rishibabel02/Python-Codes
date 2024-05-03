'''Write a program to read 3 subject marks 
and display pass or failed using class and 
object '''

eng = int(input("Enter the marks of English:"))
math = int(input("Enter the marks of Maths:"))
phy = int(input("Enter the marks of Physics:"))

class Result:
    def __init__(self,eng,math,phy):
        self.eng = eng
        self.math = math
        self.phy =phy

    def check(self):
            if self.eng > 33 and self.phy >33 and self.math>33 :
                print("Pass!!")
            else:
                print("Fail😱")

student  = Result(eng ,math , phy)
student.check()

