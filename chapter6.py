"""age = int(input("Enter your age :"))
if age>18:
    print("yes")
else:
    print("no")"""


a= [45,67,89]
print(67 in a)
print(6 in a)    

b = 65
if (b is None):
    print("yes")
else:
    print("No")

# find the greatest number 
"""num1 = int(input("Enter number1\n"))
num2 = int(input("Enter number2\n"))
num3 = int(input("Enter number3\n"))
num4 = int(input("Enter number4\n"))

if (num1>num4):
    f1=num1
else:
    f1=num4

if (num2>num3):
    f2=num2
else:
    f2=num3

if (f1>f2):
    print("The winner is :" + str(f1))
else:
    print("The winner is :" + str(f2))
"""
"""sub1 = int(input("Enter the subject marks :"))
sub2 = int(input("Enter the subject marks :"))
sub3 = int(input("Enter the subject marks :"))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif(((sub1+sub3+sub2)/3)<40):
    print("You are fail due to combined shortage")
else:
    print("Congratulations you passed ")"""


# Spam Detector
"""Spam = False
Comment = input("Enter the text")
if ("Makes a lot of money"):
    Spam = True
elif ("click here"):
    Spam = True
if (Spam):
    print("This is spam")
else:
    print("NOT Spam")"""

# username contains less than 10 characters

"""username = input("Enter the username")
if(len(username)<10):
    print("Username less than 10")
else:
    print("perfect")"""

# Find weather a given persons name is in list or not

"""list = ["bhupi","sam","lalit"]

name = input("Enter the name :")
if name in list:
    print("Your name is in the list, Welcome")
else:
    print("Please check your credentials")"""

# Program to calculate grade

"""marks = int(input("Enter your marks "))
if marks>=90:
    grade = "Excellent"
elif (marks>=80):
    grade = "A"
elif (marks>=70):
    grade = "B"
print(grade)"""

# Check weather bhupi is in the post or not

name = "bhupi"
post = input("Enter the post")
post = post.lower()
print(post)
if name in post.lower():
    print("present")
else:
    print("Absent")









