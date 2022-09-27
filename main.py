# Creating a program that calculate how many days, weeks, months we have left if we live until 90 years old.

# Obtaining input
age = input("What is your current age?")

left = 90 - int(age)

days = int(left) * 365
weeks = int(left) * 52
months = int(left) * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')