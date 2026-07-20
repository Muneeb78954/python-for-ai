################# Lists ########################
my_list = [1, 2, 3]
print(my_list)

name = "Muneeb"
age = 22
student_id = 907383
course = "Python for AI"
student_info = [name, age, student_id, course]
print(student_info)
#fetching values from list
print(student_info[0])
print(student_info[1])
print(student_info[2])
print(student_info[3])

#slicing lists
print(student_info[1:3]) #fetches values from index 1 to 2
#changing values in list
student_info[1] = 23
print(student_info)

#list methods
my_list = [1, 2, 3]
my_list.append(4)  # Add an element to the end of the list
print(my_list)  # Output: [1, 2, 3, 4]
my_list.remove(2)  # Remove the first occurrence of an element
print(my_list)  # Output: [1, 3, 4]
my_list.insert(1, 5)  # Insert an element at a specific index
print(my_list)  # Output: [1, 5, 3, 4]
my_list.pop()  # Remove and return the last element
print(my_list)  # Output: [1, 5, 3]
del my_list[0]  # Delete an element at a specific index
print(my_list)  # Output: [5, 3]

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy
print(new_list)             # [9, 5, 4, 3, 1, 1]

#checking lists
fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

if "grape" not in fruits:
    print("Grape is not in the list.")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")

############### dictionaries ########################
# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Muneeb",
    "age": 22,
    "city": "New Lahore"
}
person["name"]  # Accessing a value
person["name"] = "Ali"  # Modifying a value
person["country"] = "Pakistan"  # Adding a new key-value pair
# Different ways to create
scores = dict(math=95, english=87, science=92)

#dictionary methods
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})
person.clear()  # Remove all items
print(person)  # Output: {}

# Dictionary of dictionaries
students = {
    "alice": {
        "age": 20, 
        "grade": "A"},
    "bob": {
        "age": 21, 
        "grade": "B"},
    "charlie": {
        "age": 19, 
        "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"

############# tuples ########################
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

#accessing tuple items
point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

#tuple unpacking
# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!

########## sets ########################
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

# Basic Operations
colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")