import calculator as calc
import string_utlil as str_util

fact_result = calc.factorial(11)
print(f"Factorial of 5 is: {fact_result}")

sum_result = calc.add(10, 5)
print(f"Sum of 10 and 5 is: {sum_result}")

square_result = calc.square(11)
print(f"Square of 11 is: {square_result}")

cube_result = calc.cube(11)
print(f"Cube of 3 is: {cube_result}")

divide_result = calc.divide(10, 2)
print(f"10 divided by 2 is: {divide_result}")

str_utilresult = str_util.is_palindrome("madam")
print(f"Is 'madam' a palindrome? {str_utilresult}")

concat_result = str_util.concatenate_strings("Hello, ", "World!")
print(f"Concatenated string: {concat_result}")

length_result = str_util.string_length("Hello")
print(f"Length of 'Hello' is: {length_result}")

reverse_result = str_util.reverse_string("Hello")
print(f"Reversed string of 'Hello' is: {reverse_result}")

from calculator import add, subtract
add_result = add(20, 10)
print(f"Addition of 20 and 10 is: {add_result}")

subtract_result = subtract(20, 10)
print(f"Subtraction of 20 and 10 is: {subtract_result}")

# Using built-in functions
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
minimum_value = min(x)
maximum_value = max(x)
print(f"Minimum value in the set is: {minimum_value}")
print(f"Maximum value in the set is: {maximum_value}")

abs_value = abs(-20)
print(f"Absolute value of -20 is: {abs_value}")

# Using math module
import math
sqrt_value =math.sqrt(16)
print(f"Square root of 16 is: {sqrt_value}")

ceil_value = math.ceil(4.2)
floor_value = math.floor(4.7)
print(f"Ceiling value of 4.2 is: {ceil_value}")
print(f"Floor value of 4.7 is: {floor_value}")

# EDA - Fake Data Processing
import random
import datetime

today= datetime.date.today()
print("Today's date is:", today)  # Current date and time

now = datetime.datetime.now()
print("Current date and time is:", now)  # Current date and time

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

choice = random.choice(['apple', 'banana', 'cherry', 'date'])
print(f"Randomly selected fruit: {choice}")

random_float = random.uniform(1.0, 10.0)
print(f"Random float between 1.0 and 10.0: {random_float}")

random_sample = random.sample(range(1, 100), 5)
print(f"Random sample of 5 numbers from 1 to 100: {random_sample}")
# Note: The above code demonstrates the use of user-defined modules, built-in functions, and standard libraries in Python.
# It includes mathematical operations, string manipulations, and generating random data and dates.