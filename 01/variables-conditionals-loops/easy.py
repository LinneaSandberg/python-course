import math
import signs

# TODO: Write a Python program that calculates the area of a circle based on the radius given as a variable.
def calculate_area_of_circle(radius):
    return math.pi * radius ** 2

radius = 5
area = calculate_area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area}")


# TODO: Write a Python program that determines whether a given number is even or odd, and prints an appropriate message to the user.
def calculate_is_even_or_odd(number):
    if number % 2 == 0:
        return True
    return False

number = 74
odd = False
if calculate_is_even_or_odd(number) != odd:
    print(f"The number is {number} Even")
else:
    print(f"The number is {number} Odd")


# TODO: Write a Python program that will accept the base and height of a triangle and compute its area.
def calculate_triangle_area(base, height):
    return base * height / 2

base, height = 6, 2
triangle_area = calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is {triangle_area}")


# TODO: Write a Python program to calculate a dog's age in dog years. (For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.)
def calculate_dog_years(dog_age):
    if dog_age <= 2:
        dog_years = dog_age * 10.5
    else:
        dog_years = 2 * 10.5
        dog_years += (dog_age - 2) * 4
    return dog_years

dog_age = 4
dog_years = calculate_dog_years(dog_age)
print(f"The dog's age in dog years is: {dog_years}")


# TODO: Write a Python program to display the astrological sign for a given date of birth.
def get_astrological_sign(day, month):
    for sign, start, end in signs.astro_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return None

birth_day, birth_month = 17, 7
sign = get_astrological_sign(birth_day, birth_month)

if sign:
    print(f"The astrological sign for the born date {birth_day}/{birth_month} is: {sign}")
else:
    print("Invalid date input.")