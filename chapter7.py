# While 
"""i = 0
while i<10:
    print("yes")
    i+=1"""

# Print 1 to 50

"""i=1
while i<=50:
    print(i)
    i+=1"""

# Print five times bhupi

"""i = 0
while i<5:
    print("Bhupi")
    i+=1"""

# Print content of the list
"""fruit = ["banana","Orange","Grapes"]
i=0
while i<len(fruit):
    print(fruit[i])
    i+=1

for item in fruit:
    print(item)

for item in range(8):
    print(item)

for item in range(2,8):
    print(item)

for item in range(0,8,3):
    print(item)

for i in range(10):
   
    if i == 5:
        continue
    print(i)"""

# Print multiplication table

"""num = int(input("Enter a Number: "))
for i in range(1,11):
    print(str(num)+"X"+str(i)+"="+str(i*num))"""


# using f string
"""num = int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")"""

"""l1 = ["Harry", "Bhupi","Sam"]
for item in l1:
    if item.startswith("S"):
        print("Hello Smarty")
    else:
        print("Hello")"""

"""num = int(input("Enter a Number: "))
i =1
while i<11:
    print(f"{num} X {i} = {num*i}")
    i+=1"""

# Prime Number

"""num = int(input("Enter a Number: "))
prime = True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if prime:
    print("this is prime")
else:
    print("not prime")"""

# Factorial

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
#num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
"""if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)"""

   






