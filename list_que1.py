# list = [1,2,3,4,5,6]
# even_sum = sum(x for x in list if x%2==0)
# print(even_sum)

# Take input from the user for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
my_list = [int(num) for num in user_input.split()]


result = sum(num for num in my_list if num % 2 == 0)


print("Sum of even numbers:", result)
