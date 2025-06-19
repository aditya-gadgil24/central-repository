# Shree

# lists data structure in python

# Using Square Brackets []

my_list = [1, 2, 3, "hello", 3.14]
empty_list = []

# Using the list() constructor
my_list2 = list((1, 2, 3)) # from a tuple
my_list3 = list("python") # from a string


# Accessing Elements
# Indexing: You can access individual elements using their index, starting from 0 for the first element

my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10
print(my_list[2])  # Output: 30

# Negative Indexing: Negative indices access elements from the end of the list, with -1 being the last element

print(my_list[-1]) # Output: 40
print(my_list[-2]) # Output: 30

# Slicing: You can extract a portion of a list using slicing
print(my_list[1:3])  # Output: [20, 30]
print(my_list[:2])   # Output: [10, 20]
print(my_list[2:])   # Output: [30, 40]
print(my_list[::2])  # Output: [10, 30] every second element

# Modifying Lists
# Changing Elements
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30, 40]

# Adding Elements
# append(): Adds an element to the end of the list
my_list.append(50)
print(my_list) #output: [10, 25, 30, 40, 50]

# insert(index, element): Inserts an element at a specific index
my_list.insert(2, 35)
print(my_list) #output: [10, 25, 35, 30, 40, 50]

# extend(another_list): Appends all elements from another list to the end
other_list = [60, 70]
my_list.extend(other_list)
print(my_list) #output: [10, 25, 35, 30, 40, 50, 60, 70]

# Removing Elements
# remove(element): Removes the first occurrence of a specific element
my_list.remove(35)
print(my_list) #output: [10, 25, 30, 40, 50, 60, 70]

# pop(index): Removes and returns the element at a specific index (or the last element if no index is provided)

removed_element = my_list.pop(3)
print(my_list) #output: [10, 25, 30, 50, 60, 70]
print(removed_element) #output: 40

# del list[index] or del list[start:end] : deletes the element at the specified index or deletes a slice of the list

del my_list[0]
print(my_list) #output: [25, 30, 50, 60, 70]
del my_list[1:3]
print(my_list) #output: [25, 60, 70]


# clear(): Removes all elements from the list
my_list.clear()
print(my_list) #output: []

# List Operations
# Concatenation (+): Combines two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition (*): Repeats a list a specified number of times
repeated_list = list1 * 3
print(repeated_list) #output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# len(list): Returns the number of elements in a list.
# in and not in: Checks if an element is present or not present in a list
print(3 in list1) #output: True
print(7 in list1) #output: False

# count(element): Returns the number of times an element appears in a list.
# index(element): Returns the index of the first occurrence of an element.
# sort(): Sorts the list in ascending order (in place).
# reverse(): Reverses the list (in place).
# copy(): returns a shallow copy of a list.

# List Comprehensions
# List comprehensions provide a concise way to create lists

squares = [x**2 for x in range(10)] #creates a list of squared numbers 0-9
print(squares) #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x**2 for x in range(10) if x%2==0] 
#creates a list of even squared numbers 0-9.
print(even_squares) #output: [0, 4, 16, 36, 64]

even_squares = [x**2 for x in range(10) if x%2==0] 
#creates a list of even squared numbers 0-9.
print(even_squares) #output: [0, 4, 16, 36, 64]

# end of code block
