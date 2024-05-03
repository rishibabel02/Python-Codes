# l = [4,5,6,7]

# print(l[0:3])
# print(l[len(l) - 1])
# print(l[0:-2])
# print(l[::-1])

'''Accepting 5 values '''

# values = []
# for i in range(5):
#     val = int(input("Enter the value: "))
#     values.append(val)

# similar = {}
# for i , val in enumerate(values):
#     if val in similar :
#         similar[val].append(i)
#     else:
#         similar[val] = [i]



'''sort'''
# l = []
# for i in range(5):
#     val = int(input("Enter the numbers: "))
#     l.append(val)

# l.sort(reverse=True)
# x = len(l)
# print(l)
# print(x)


'''Acronym'''

# def acr(phrase):
#     words = phrase.split()
#     acronym = ' '
#     for word in words:
#         acronym += word[0].upper() 
#     return acronym

# def main():
#     phrase = input("Enter the phrase: ")
#     acronym = acr(phrase)
#     print(acronym)

# if __name__ == "__main__":
#     main()
   
'''Month'''

def get_month_abbreviation(month_number):
    month_abbreviations = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return month_abbreviations.get(month_number, "Invalid month number")

# Get input from user
month_number = int(input("Enter the month number (1-12): "))

# Print the abbreviation of the month
print("Abbreviation:", get_month_abbreviation(month_number))



'''20 Values Wala'''

def even_nums(nums):
    return (len([num for num in nums if num%2==0]))
def odd_nums(nums):
    return (len([num for num in nums if num%2==1]))
def positive_nums(nums):
    return (len([num for num in nums if num>0]))
def negative_nums(nums):
    return (len([num for num in nums if num<0]))

nums=list(map(int,input("Enter 20 elements(separated by space):").split()))
count_even=even_nums(nums)
count_odd=odd_nums(nums)
count_positive=positive_nums(nums)
count_negative=negative_nums(nums)

print(f"Total Even:{count_even}\tTotal Odd:{count_odd}\n")
print(f"Total Positive:{count_positive}\tTotal Negative:{count_negative}")



