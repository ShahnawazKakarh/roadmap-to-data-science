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


