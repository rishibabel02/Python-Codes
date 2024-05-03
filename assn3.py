'''Write a python program that accepts the length of three sides of a triangle as inputs.
The program should indicate whether or not the triangle is a right-angled triangle using function 
with exception handling'''


def right_angled(a,b,c):
    sides = [a,b,c]
    sides.sort()

    if sides[0]<=0:
        raise ValueError("Enter +ve side length!")
    elif sides[0]+sides[1]<=sides[2]:
        raise ValueError("The side lengths you entered can't form a triangle.")
    
    for_right_angle = sides[0]**2 + sides[1]**2 == sides[2]**2
    return for_right_angle

if __name__ == "__main__":
    
        a = float(input("Enter the length of side a:"))
        b = float(input("Enter the length of side b:"))
        c = float(input("Enter the length of side c:"))

        if right_angled(a,b,c):
            print("The triangle is right angled.")
        else:
             print("The triangle is not right angled.")
   
    