def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def root(a):
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    return a ** 0.5

def power(a, b):
    return a ** b

def trigonometric_sine(angle):
    import math
    return math.sin(math.radians(angle))

