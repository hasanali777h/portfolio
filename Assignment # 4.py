'''# Q1) Question1:Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.
# Add a new key value pair about qualification then update the qualification value to high academic level then delete it.

d_info = {"first_name": "hasan", "last_name": "ali", "age": 27, "city": "khi"}
# print(d_info.keys())
d_info["qualification"] = "intermediate level"
d_info.update(qualification="high level")
print(d_info)
del d_info["qualification"]
print(d_info)

# Q2)Question2:Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it.
info_city1 = {"c_name1": "karachi", "country": "pakistan", "population": 15741000,
              "fact": "Karachi has the largest mall of Asia"}
info_city2 = {"c_name2": "melbourne", "country": "australia", "population": "4.8 million",
              "fact": "Port Melbourne is the only place in the world that makes Vegemite."}
info_city3 = {"c_name3": "moscow", "country": "russia", "population": "12.412 Million",
              "fact": "Moscow is named after a river"}
print(info_city1.values())
print(info_city2.values())
print(info_city3.values())

# Q3)Question3:A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# and then tell them the cost of their movie ticket.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age <= 3:
        print("  You get in free!")
    elif age > 3 and age <= 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


# Q4)Question4:Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is Alice in Wonderland.
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    aouther1_name = "aouther1"
    aouther2_name = "aouther2"
    aouther3_name = "aouther3"
    x = input("enter aouther name to check favorite book: ")
    if x == "aouther1":
        print("my favorite book is: ", title)
    elif x == "aouther2":
        print("my favorite book is: ", title)
    elif x == "aouther3":
        print("my favorite book is: ", title)
    else:
        print("book not found")


favorite_book("Beauty and the beast")
favorite_book("Alaadin")
favorite_book("Loin king")
# Q5)Question5:Guess the number game.
# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number.
# Give three chances to user guess the number and also give hint to user if hidden number is greater or smaller than the number he given to input field.

import random

for i in range(10):
    x = random.randint(1, 30)
    i = random
    print(x)
guess = int(input("enter your guessed no.: "))
if guess == x:
    print("CORRECT...!!!")
elif guess < x:
    print("TOO LOW...")
elif guess > x:
    print("TOO HIGH...")
else:
    print("wrong move...")'''
