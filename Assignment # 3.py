'''# Q1) 1. Make a calculator using Python with addition , subtraction , multiplication , division and power.
import math

print("CALCULATOR \n To do some calculation select an operation \n")
print("add, sub, mul, div, pow")
op = "+", "-", "*", "/", "pow"
val_1 = int(input("enter first value: "))
val_3 = input("enter an operand: ")
val_2 = int(input("enter second value: "))

if val_3 == "+":
    print("Addition result: ", val_1, "added in", val_2, "=", val_1 + val_2)
elif val_3 == "-":
    print("Subtraction result: ", val_1, "minus from", val_2, "=", val_1 - val_2)
elif val_3 == "*":
    print("Multiplication result: ", val_1, "multiplied by", val_2, "=", val_1 * val_2)
elif val_3 == "/":
    print("Division result: ", val_1, "divided by", val_2, "=", val_1 / val_2)
elif val_3 == "pow":
    print("Power is: ", val_1, "exponent(power)", val_2, "=", val_1 ** val_2)
else:
    print("Invalid inputs")

# Q2) 2. Write a program to check if there is any numeric value in list using for loop

a = []
x = int(input("enter range of element to put in list: "))
for i in range(0, x):
    x = int(input("enter value here: "))
    a.append(x)
    print(a)
    j = int(input("enter index value to find value in list"))
    if j in a:
        a.index(j)
        print("The numeric value is at index: ", a.index(j))
    else:
        print("not found")

# Q3) 3. Write a Python script to add a key to a dictionary

my_dict = {"hasan": 1, "ali": 2, "mushii": 3}
new_dict = {input("enter value: "): int(input("enter key"))}
my_dict.update(new_dict)
print(my_dict)
# Q4)4. Write a Python program to sum all the numeric items in a dictionary
d = {4: 1, 10: 2, 55: 3, 57: 4, 88: 5}
print("The sum of numeric values in dict is: ", sum(d))
# Q5) 5. Write a program to identify duplicate values from list
import collections

a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
print([item for item, count in collections.Counter(a).items() if count > 1])
# Q6) 6. Write a Python script to check if a given key already exists in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
x = input("enter value to check key exist or not: ")
if 'a' == x:
    print("key exits ")
elif 'b' == x:
    print("key exits ")
elif 'b' == x:
    print("key exits ")
else:
    print("key not exits ")'''
