answer = input("Want to know when you will be 30? ")
print()
if answer == 'Yes' or 'Y' or 'yes' or 'y' or 'sure': 
    print("Great!")
else: 
    print("Let's see how old you really are!")
print()
birthday_month = input("When is your birth month? ")
print()
age = int(input("What is your age? "))
print()
birth_year = int(input("What year were you born? "))
print()
print(f"You are {age} years old.")
if age > 30:
    print(f"Your birth month is {birthday_month} and "
          f"this year is 2024. That means you turned "
          f"30 in {abs(age - 2024)}.")
else:
    print(f"Your birth month is {birthday_month} and "
          f"this year is 2024. That means you will "
          f"turn 30 in {birth_year + 30}. ")
print()
if birth_year < 2005:
    print("Wow, you're really old...")
else:
    print()