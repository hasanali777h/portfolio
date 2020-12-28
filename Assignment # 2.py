#1. Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?
'''eng_marks = int(input("enter marks of english: "))
print("your marks of english course are: ", eng_marks)
maths_marks = int(input("enter marks of maths: "))
print("your marks of maths course are: ", maths_marks)
phys_marks = int(input("enter marks of physics: "))
print("your marks of physics course are: ", phys_marks)
chem_marks = int(input("enter marks of chemistry: "))
print("your marks of chemistry course are: ", chem_marks)
bio_marks = int(input("enter marks of biology: "))
print("your marks of biology course are: ", bio_marks)
cosmo_marks = int(input("enter marks of cosmology: "))
print("your marks of cosmology course are: ", cosmo_marks)
comp_marks = int(input("enter marks of computer sci.: "))
print("your marks of computer sci. course are: ", comp_marks)
total_marks = eng_marks+maths_marks+phys_marks+chem_marks+comp_marks+cosmo_marks+bio_marks
print("total marks are: ", total_marks)
per = total_marks * 100 / 700
print("your percentage is: ", per)
print("your grade is: ")
if per >= 80:
    print("A+")
elif 70 <= per < 80:
    print("A")
elif 60 <= per < 70:
    print("B")
elif 50 <= per < 60:
    print("C")
else:
    print("F")

#2. Write a program which take input from user and identify that the given number is even or odd?
var = int(input("enter a number to check it is even or odd: "))
if var %2 == 0:
    print("it's a even number")
else:
    print("its's a odd number")

#3. Write a program which print the length of the list?
list_1 = len([1, 2, 3, 4, 5, 'a', 'b', 'c', 'x', 'y', 'z'])
print(list_1)
#OR
list_1 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'x', 'y', 'z']
print(len(list_1))

#4. Write a Python program to sum all the numeric items in a list?
lst = sum([12, 22, 31, 17, 92])
print(lst)
#OR
lst_1 = []
r = int(input("enter the range of list here: "))
for i in range(r):
    var = int(input("enter value here: "))
    lst_1.append(var)
    print("sum of list elements are: ", sum(lst_1))

#5.(A) Write a Python program to get the largest number from a numeric list.
my_list = max([11,333,6,1080,320,77,62])
print(my_list)
#5.(B) Write a Python program to get the smallest number from a numeric list.
my_list = min([11,333,6,1080,320,77,62])
print(my_list)

#6. Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
for i in a:
    if i < 5:
        x.append(i)
        print(x)
'''
