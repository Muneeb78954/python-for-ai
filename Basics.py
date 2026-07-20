############################### Variables ######################################
name = "Muneeb"
age = 22
is_student = True
height = 5.5
course = "python for AI"

#Same value to different variables
x = y = z = 10

#unpacking variables
a, b, c = 1, 2, 3
Pm , Cm = "Shehbaz Sharif", "Imran Khan"

################################### Data types #####################################
string_var = "Hello, World!"
#string adding 
first_name = "Muneeb"
last_name = "Khan"
full_name = first_name + " " + last_name #string concatenation
long_dash = "-" * 30 #string repetition
print(len(string_var)) #length of string
first_name = "Jane"
last_name = "Doe"
greeting = f"Hello, {first_name} {last_name}!"
print(greeting)
#string methods
print(string_var.upper())  # Convert to uppercase
print(string_var.lower())  # Convert to lowercase
print(string_var.strip())  # Remove leading and trailing whitespace
print(string_var.title())  # Convert to title case  
print(string_var.replace("World", "Python"))  # Replace substring
message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)


#Integers
integer_var = 42
#arithmetic operations
print(2 + 2) #integer addition
print(5 - 3) #integer subtraction
print(4 * 6) #integer multiplication
print(10 / 2) #integer division    
print(10 // 3) #floor division
print(10 % 3) #modulus operator
print(10 ** 2) #exponentiation operator
result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)
print(result)

#logical operators
# AND - both must be true
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(can_drive) #True
# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False


float_var = 3.14
complex_var = 2 + 3j #complex number

#True or False values
boolean_var = True

age = 17
can_vote = age >= 18 #comparison operator returns boolean value
print(can_vote) #False

#comparison operators
age = 25

# Equality
print(age == 25)     # True - equals
print(age != 30)     # True - not equals

# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal



#sequence data types
list_var = [1, 2, 3] #mutable ordered list
tuple_var = (4, 5, 6) #immutable ordered list
range_var = range(10) #immutable sequence of numbers

#mapping data types
dictionary_var = {"name": "Muneeb", "age": 22} #unordered collection of key-value pairs like key-value pairs
NoneType_var = None

#set types
set_var = {7, 8, 9} #unordered collection of unique elements
frozenset_var = frozenset([10, 11, 12]) #immutable unordered collection of unique elements

#checking data types
print(type(string_var))

#Control flow statements
# if-elif-else statement
score = 100

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")
#multiple conditions
age = 25
has_license = True

# Both must be True
weekend = True
holiday = False
raining = False
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")
#nested if statements
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")
############################### Loops #####################################
for i in range(10):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2): #step of 2
    print(i)