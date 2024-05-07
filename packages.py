""""
math_operations/
├── __init__.py
├── addition.py
└── multiplication.py

"""
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y
## Now going to main

## get the package
from math_operations import addition, multiplication

## getting the results 
addition_results = addition.add(3, 5)
print("Addition result is:", addition_results )

multiplication_results = multiplication.add(3, 5)
print("multiplication result is:", multiplication_results )