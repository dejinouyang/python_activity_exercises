# Task
# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n .

# Constraints
# 1 ≤ n ≤ 100

# Output Format
# Print "Weird" if the number is weird. Otherwise, print "Not Weird".

# Code Below:

#!/bin/python3

# Importing some useful libraries
# Test your code: python -m Tests.test_level2



def solution(n):
    if n % 2 == 1: 
        return "Weird"
    elif 2 <= n <= 5:  
        return "Not Weird"
    elif 6 <= n <= 20:  
        return "Weird"
    elif n > 20:  
        return "Not Weird"


if __name__ == '__main__':
    n = int(input().strip())  # This line will read an integer inserted by the user and store it into a variable called n, which is then passed to your solution function as an argument

    print(solution(n))  # calls the solution function with the value you insert
