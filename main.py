# This is a practice on Python.
import turtle

input1 = int(input("Enter a number: "))
input2 = int(input("Enter a number: "))
input3 = int(input("Enter a number: "))
input4 = int(input("Enter a number: "))

print("This is your average: ") + str((input1 + input2 + input3 + input4) / 4)

total = int(input("What is your total bill?"))
diners = int(input("How many diners ate this meal?"))

print("This is how much each person should pay: " + str(total / diners))