# a = [1,2,3,4,5,6,7,8,9]
# print(a[::2]) #[start:stop:step]

# l = [1,2,3]
# init_tuple = ('Python',) * (l.__len__() -1)
# print(init_tuple)

# dict: unordered collection of key-value  pair
# list: ordered mutable sequence of element

def dictionary_operations():
    # Create a dictionary
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print("Initial Dictionary:", my_dict)

    # Add a new key-value pair
    my_dict['occupation'] = 'Engineer'
    print("After adding 'occupation':", my_dict)

    # Update an existing value
    my_dict['age'] = 32
    print("After updating 'age':", my_dict)

    # Remove a key-value pair
    del my_dict['city']
    print("After removing 'city':", my_dict)

    # Iterate over keys and values
    print("Iterating over keys and values:")
    for key, value in my_dict.items():
        print(key, ":", value)

def tuple_operations():
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("\nInitial Tuple:", my_tuple)

    # Access elements
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])

    # Concatenate tuples
    new_tuple = my_tuple + (6, 7)
    print("Concatenated Tuple:", new_tuple)

    # Slice tuple
    sliced_tuple = my_tuple[1:4]
    print("Sliced Tuple:", sliced_tuple)

    # Convert tuple to list
    list_from_tuple = list(my_tuple)
    print("List from Tuple:", list_from_tuple)

def main():
    print("Dictionary Operations:")
    dictionary_operations()

    print("\nTuple Operations:")
    tuple_operations()

if __name__ == "__main__":
    main()
