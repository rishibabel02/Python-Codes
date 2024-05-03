' Write a python program to find largest of three numbers'

# a = int(input("Enter 1st no."))
# b = int(input("Enter 2nd no."))
# c = int(input("Enter 3rd no."))

# if(a>b and a>c):
#     print(a,"is the largest of all")
# elif(b>a and b>c):
#     print(b,"is the largest of all")
# else:
#     print(c,"is the largest of all")

#OR

# largest  = max(a,b,c)
# print(f"The largest no is {largest}")

'''Write a python program to accept Marks in Math and display respective grade as 
an output using if…elif…elif..else statements (Using multiple conditions)'''

marks = int(input("Enter the Marks of Math:"))

if(marks>=90 and marks<100 ):
    print("O")
elif(marks>=80 and marks<89):
    print("A+")
elif(marks>=70 and marks<79):
    print("A")
elif(marks>=60 and marks<69):
    print("B")
elif(marks>=50 and marks<59):
    print("C")
elif(marks>=40 and marks<49):
    print("P")
elif(marks<=39):
    print("F")
else:
    print("Enter valid Marks!")