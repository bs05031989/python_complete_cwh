"""def percent(marks):
    return ((marks[0]+marks[1])/200)*100

marks1 = [23,44]

print(percent(marks1))"""

# Default parameter value
"""def greet(name = "stranger"):
    print("Good day"+ name)

greet("bhupi")
greet()


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


print(recur_factorial(5))"""

def convert (cel):
    return (cel*(9/5)+32)

print(convert(45))

def sum(n):
    if n == 1:
       return n
    else:
       return sum(n-1)+n

print(sum(5))



