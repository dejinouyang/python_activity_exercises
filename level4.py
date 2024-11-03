# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example

# The result of the integer division 3 // 5 = 0.
# The result of the float division is 3 / 5 = 0.6.

# Test your code: python -m Tests.test_level4

def solution(num1, num2):
    int_division = num1 // num2  
    float_division = num1 / num2  
    return int_division, float_division 



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_result, float_result = solution(a, b)
    print(int_result)   #
    print(float_result)  
