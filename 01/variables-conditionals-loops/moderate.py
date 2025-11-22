import math

# TODO: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for number in range(7):
    if number != 3 and number != 6:
        print(number)


# TODO: Write a Python program to get the Fibonacci series between 0 and 50.
def fibonacci(num):
    fib_numbers = []
    a, b = 0, 1
    for _ in range(num):
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

num = 50
print(f"Fibonacci numbers from 0-50 are: {fibonacci(num)}")


# TODO: Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
def greatest_common_divisor(num1, num2):
    return math.gcd(num1, num2)

num1, num2 = 74, 56
print(f"The GCP of {num1} and {num2} is {greatest_common_divisor(num1, num2)}")


# TODO: Write a Python program to find the least common multiple (LCM) of two positive integers.
def least_common_multiple(num1, num2):
    return math.lcm(num1, num2)

num1, num2 = 5, 32
print(f"The LCM of {num1} and {num2} is {least_common_multiple(num1, num2)}")