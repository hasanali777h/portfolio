#guessing a random number
'''import random
for i in range(10):
    x = random.randint(0, 21)
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


'''# sin and cos graph making
import numpy as np
import matplotlib.pyplot as plt
# if using a jupyter notebook (%matplotlib inline)
#x = np.arange(0, 4*np.pi, 0.1) # start,stop,step
#y = np.sin(x)
#z = np.cos(x)
x = np.arange(0, 4*np.pi-1, 0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.xlabel('x values from 0 to 4pi') # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)']) # legend entries as separate strings in a list
plt.plot(x, y, x, z)
plt.show() '''
""""plt.xlabel()	x-axis label	plt.xlabel('x values from 0 to 4pi')
                  plt.ylabel()	y-axis label	plt.ylabel('sin(x) and cos(x)')
                  plt.title()	plot title	plt.title('Plot of sin and cos from 0 to 4pi')
                  plt.legend([ ])	legend	plt.legend(['sin(x)', 'cos(x)'])"""

'''# password generator
import string
import random
x = string.ascii_letters
print(x)
y = string.digits
print(y)
z = string.punctuation
print(z)
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(random.choice(characters) for x in range(random.randint(8, 16)))
print(password)
'''
