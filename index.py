# Python If-Else
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
def test(n):
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

# Arithmetic Operators
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.


def arithmetic_operators(a: int, b: int):
    print(a + b)
    print(a - b)
    print(a * b)

# Python: Division
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.


def division(a: int, b: int):
    print(a // b)
    print(a / b)

# Loops


def loops(n):
    for number in range(n):
        print(pow(number, 2))

# Write a Function


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return leap
    elif year % 4 == 0:
        leap = True

    return leap


# Print Function
if __name__ == '__main__':
    n = int(input())

    result = ''
    for numbers in range(n):
        result += str(numbers + 1)
    print(result)

# List Comprehensions


def create_list(x, y, z, n):
    print(n)


print(create_list(2, 2, 2, 2))
