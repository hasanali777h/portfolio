'''# Question:1
def factorial(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    print("The factorial of", num, "is", factorial)


factorial(5)


# Question:2

def upperCaseLowerCase(string):
    count1 = 0
    count2 = 0
    for i in string:

        if (i.islower()):
            count1 = count1 + 1
        elif (i.isupper()):
            count2 = count2 + 1

    print("The number of lowercase characters is:")
    print(count1)
    print("The number of uppercase characters is:")
    print(count2)


upperCaseLowerCase("HeLLo")

# Question: 3

list1 = [10, 21, 4, 45, 66, 93]


# iterating each number in list
def checkEven(list):
    for num in list:

        # checking condition
        if num % 2 == 0:
            print(num, end=" ")


checkEven(list1)


# Question:4

# function to check string is
# palindrome or not
def isPalindrome(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False


# main function
s = "madam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")


# Question:5
def primeNumber(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
            else:
                print(num, " is a prime number")

    else:
        print(num, "is not a prime number")


primeNumber(5)


# Question:6
def shoppingItems(*items):
    print("Shopping Items: \n")
    for item in items:
        print(item)


shoppingItems("Milk", "Tea", "Meat", "Oil")'''
