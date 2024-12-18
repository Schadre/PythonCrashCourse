# Tasks:
# 1. Dictionaries:
#     Create a dictionary to store information about three friends, such as
#     their name, favorite hobby, and favorite food. Print each person's
#     information in a clean format(Chapter 6).

friends = {
    "Saint": {"Favorite hobby": "weight lifting", "Favorite food": "seafood"},
    "Nick" : {"Favorite hobby": "modeling", "Favorite food": "pasta"},
    "Joelle": {"Favorite hobby": "making money", "Favorite food": "steak"},
    }

for friend, friend_info in friends.items():
    print(f"{friend}'s favorite hobby is {friend_info['Favorite hobby']} and {friend}'s favorite food is {friend_info['Favorite food']}.")


# 2. UserInput:
#     Write a program that asks for the user's age and prints a message
#     based on whether they are a child, teenager, or adult(Chapter 7).

age = int(input("How old are you? "))

def age_verification(age):
    if age <= 12:
        print("Minor")
    elif age <= 17:
        print("Teenager")
    elif age >= 18:
        print("Adult")

age_verification(age)


# 3. Functions:
#     Create a function that takes two numbers as arguments and returns
#     their product. Write another function that takes a list of numbers and
#     returns the sum of allthe numbers in the list(Chapter 8).

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def numbers_game(a , b):
    c = a + b
    print(f"{a} + {b} = {c}")
    d = a - b
    print(f"{a} - {b} = {d}")
    e = a * b
    print(f"{a} * {b} = {e}")
    f = a / b 
    print(f"{a} / {b} = {f}")

numbers_game(a, b)