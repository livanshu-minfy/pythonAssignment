# ------------------------------------------------------ EASY QUESTIONS ------------------------------------------------------


'''
Function Basics
Write a function called calculate_average that takes a list of numbers as input and returns their average. If the list is empty, it should return 0.'''

def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)


# Example usage:
print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))  # Should return 0

'''
Default Parameters
Write a function called `greet_user` that takes a name and a greeting message. The greeting message should default to "Hello" if not provided.'''

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage:
print(greet_user("Alice"))# Should return "Hello, Alice!"
print(greet_user("Bob", "Hi")) # Should return "Hi, Bob!"


# ------------------------------------------------------ MEDIUM QUESTIONS ------------------------------------------------------

'''
Variable Arguments
Create a function called `calculate_total` that calculates the total cost of items with a variable number of prices and an optional discount percentage.'''

def calculate_total(*cost, discount = 0):
    total = sum(cost)
    if discount:
        total -= total * discount / 100
    return total

# Example usage:
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54 (10% off)


'''
Closures
Create a function called `create_multiplier` that takes a number and returns a function that multiplies any input by that number.'''

def create_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15

# ------------------------------------------------------ HARD QUESTIONS ------------------------------------------------------

'''
Recursion
Implement a recursive function called `power` that calculates x^n (x raised to the power of n) without using the built-in power operator or function. Your function should have O(log n) time complexity.'''

def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

# Example usage:
print(power(2, 10))  # 1024
print(power(3, 4))   # 81


'''
Higher-Order Functions
Create a function called `compose` that takes any number of single-parameter functions as input and returns a new function that applies each function in sequence from right to left.'''

def compose(*funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed

# Example usage:
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x ** 2

f = compose(square, double, add_one)
print(f(3))  # square(double(add_one(3))) = square(8) = 64
