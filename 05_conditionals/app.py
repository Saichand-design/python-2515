#simple condition check 
# 5 > 2 --> true 
# 2 > 5 --> False

from unittest import case


if 5>2: 
    print("5 is greater than 2")
    print("next statement")

#print("5 is greater than 2")

# if statement 
# if condition:
# statement

num = -5
if num > 0:
    print("positive Number")

    # tell me conditional to check if the given number is in range
    # 10 - 20 
    if num >= 10 and num<= 20:
        print(f"the given number {num} is in range")


#if-else statement
# if condition:
#statement
#else 
#statement
num = -10
if num > 0:
    print ("postive Number")

else:
    print("negative Number")

#vote app
age = 25 
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")

#input function demo
#name = input("enter your name:")
#age = input("enter your age:")
#print(f"welcome: {name} your age is {age}")

#vote app dynamic
#apply type casting 
age = int(input("enter your age:"))
print(type(age))
if age >= 18:
    print ("you can vote")
else :
    print ("you cannot Vote")

#ternary Operators
#value_if_true if conditional else value_if_false
#age = int(input("enter your age:"))
#vote_status = "you can vote"

mark = int(input("enter your marks:"))
if mark>= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark>=60:
    print("C")
elif mark>=50:
      print("D")
else:
    print("FAIL")

#vote app with id card
has_id = False
age = int(input("enter your age :"))
nationality = input("enter your nationality:")
if age >= 18 and nationality == "indian":
    print("you can vote")
else :
    print("you cannot vote")

#match-case syntax
choice = 2
case 1 : # type: ignore
print("one")
case 2 : # type: ignore
print("two")
case 3: # type: ignore
print("three")

print("invail")








