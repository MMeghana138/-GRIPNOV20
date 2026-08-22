#1) Create a list
# my_list = [1, 2, 3, 4, 5]
# print(my_list)

#2) Access elements in a list
# my_list = [1, 2, 3, 4, 5]
# print(my_list[0])  # Access the first element
# print(my_list[-1])  # Access the last element
# print(my_list[2:4])  # Access elements from index 2 to 3

#3) Modify elements in a list
# my_list = [1, 2, 3, 4, 5]
# my_list[0] = 10  # Modify the first element
# print(my_list)    

#4) Add elements to a list
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)  # Add an element to the end
# print(my_list)    

#5) Remove elements from a list
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)  # Remove the element 3
# print(my_list)        

#6) Iterate through a list
# my_list = [1, 2, 3, 4, 5]
# for element in my_list:
#     print(element)    

#7) List comprehension
# my_list = [1, 2, 3, 4, 5]
# new_list = [x * 2 for x in my_list]
# print(new_list)

#8) Check if an element exists in a list
# my_list = [1, 2, 3, 4, 5]
# if 3 in my_list:
#     print("Element exists in the list")
# else:
#     print("Element does not exist in the list")

#9) Sort a list
# my_list = [5, 2, 9, 1, 5, 6]
# my_list.sort()  # Sort the list in ascending order
# print(my_list)        

#10) Reverse a list
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()  # Reverse the list
# print(my_list)        

#11) Find the length of a list
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))

#12) Clear a list
# my_list = [1, 2, 3, 4, 5]
# my_list.clear()  # Clear the list
# print(my_list)        

#13) Copy a list
# my_list = [1, 2, 3, 4, 5]
# new_list = my_list.copy()
# print(new_list)

#14) Count occurrences of an element in a list
# my_list = [1, 2, 3, 4, 5, 2, 3, 2]
# count = my_list.count(2)  # Count occurrences of 2
# print(count)

#15) Find the index of an element in a list
# my_list = [1, 2, 3, 4, 5]
# index = my_list.index(3)  # Find the index of element 3
# print(index)

#16) Extend a list with another list
# my_list = [1, 2, 3]
# other_list = [4, 5, 6]
# my_list.extend(other_list)
# print(my_list)

#17) Insert an element at a specific index in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 10)  # Insert 10 at index 2
# print(my_list)

#18) Remove an element at a specific index in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.pop(2)  # Remove the element at index 2
# print(my_list)    

#19) Create a list of even numbers using list comprehension
# even_numbers = [x for x in range(1, 21) if x % 2 == 0]
# print(even_numbers)   

#20) Create a list of squares of numbers using list comprehension
# squares = [x**2 for x in range(1, 11)]
# print(squares)   

#21) Create a list of strings and sort them alphabetically
# fruits = ['banana', 'apple', 'cherry', 'date']
# fruits.sort()
# print(fruits)     

#22) Create a list of strings and sort them by length
# fruits = ['banana', 'apple', 'cherry', 'date']
# fruits.sort(key=len)
# print(fruits)         

#23) Create a list of numbers and find the maximum and minimum values
# numbers = [5, 2, 9, 1, 5, 6]
# max_value = max(numbers)
# min_value = min(numbers)
# print(f"Maximum value: {max_value}")
# print(f"Minimum value: {min_value}")

#24) Create a list of numbers and calculate the sum and average
# numbers = [5, 2, 9, 1, 5, 6]
# total_sum = sum(numbers)
# average = total_sum / len(numbers)
# print(f"Total sum: {total_sum}")
# print(f"Average: {average}")

#25) Create a list of numbers and filter out the even numbers
# numbers = [5, 2, 9, 1, 5, 6]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)