# Tasks:

# 1. List Comprehensions:
#   Create a list of numbers from 1 to 10,then use a list comprehension to
#   create another list of their squares.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_squared = [number**2 for number in numbers]
print(numbers_squared)


# 2. Conditional Logic:
#   Write a Python program that checks if a number is odd or even and
#   prints a message based on the result.

for number in numbers_squared:
    if number % 2 != 0:
        print("Odd")
    else:
        print("Even")


# 3. Pizza Toppings Program:
#   Write a program that asks the user for their favorite pizza toppings,
#   append each topping to a list and print all the toppings they entered
#   with a for loop.

choice = input("What are your favorite pizza toppings? ")

def pizza_topping(choice):
    pizza = []
    pizza.append(choice)
    for topping in pizza:
        print(topping)

pizza_topping(choice)
    