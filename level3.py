# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# You should create 3 functions one for each calculation name them (sum, sub, mult) respectively

# Example

# a = 3
# b = 5
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

# Print the following:
# 8
# -2
# 15
# Test your code: python -m Tests.test_level3


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(sum(a, b))   
    print(sub(a, b))   
    print(mult(a, b))
