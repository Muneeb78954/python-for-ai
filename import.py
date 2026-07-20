import pandas as pd


# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)

sqrt(16)

# Import entire module
import random

# Use module functions
number = random.randint(1, 100)
choice = random.choice(["apple", "banana", "orange"])
print(f"Random Number: {number}")
print(f"Random Choice: {choice}")

# Date and time
import datetime
today = datetime.date.today()
print(today)  # Output: 2024-06-15 (or the current date)

import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 30}