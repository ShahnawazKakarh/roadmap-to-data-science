def square(num):
    return num * num

def cube(num):
    return num * num * num

def power(num, exp):
    return num ** exp

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def factorial(num):
    if num < 0:
        return "Error! Factorial of negative number doesn't exist."
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

'''
def modulus(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
    
def sqrt(num):
    if num < 0:
        return "Error! Square root of negative number doesn't exist."
    return num ** 0.5

def cbrt(num):
    if num < 0:
        return -(-num) ** (1/3)
    return num ** (1/3)

def nth_root(num, n):
    if num < 0 and n % 2 == 0:
        return "Error! Even root of negative number doesn't exist."
    return num ** (1/n)

def percentage(part, whole):
    if whole == 0:
        return "Error! Division by zero."
    return (part / whole) * 100

def to_radians(degrees):
    import math
    return degrees * (math.pi / 180)

def to_degrees(radians):
    import math
    return radians * (180 / math.pi)

def sin(degrees):
    import math
    return math.sin(to_radians(degrees))

def cos(degrees):
    import math
    return math.cos(to_radians(degrees))

def tan(degrees):
    import math
    return math.tan(to_radians(degrees))

def cot(degrees):
    import math
    tan_value = math.tan(to_radians(degrees))
    if tan_value == 0:
        return "Error! Cotangent undefined."
    return 1 / tan_value

def sec(degrees):
    import math
    cos_value = math.cos(to_radians(degrees))
    if cos_value == 0:
        return "Error! Secant undefined."
    return 1 / cos_value
'''