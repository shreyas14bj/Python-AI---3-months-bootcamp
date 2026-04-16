# Variables are the labelled storage boxes where data is stored and reused.
name = "Shreyas" # String
age = 22 # int
height = 5.6 # float
isEngineer = True # boolean

print(f"Hi {name}, you are {age} years old and you are the Engineer : {isEngineer}")
print(f"Your height is {height}")

# Input system for user interaction
name = input("Enter your name: ") # Gives only string data type value
age = int(input("Enter your age: ")) # Gives int data type value

print(f"Hey {name}, you are {age} years old.")

# Operations - BEDMAS -> Bracket, Exponent, Division, Multiplication, Addition, Subtraction

# logical operations - not, and, or

# Conditional statements (Decision making)

# Salary improvement
# user input
salary = int(input("Enter salary: "))
# conditions
if salary > 30000:
    print("Good income")
else:
    print("Need improvement")

# Grade
marks = int(input("Enter the mark: "))
if marks > 90 and marks <= 100:
    print("Grade: A")
elif marks > 80 and marks < 90:
    print("Grade: A")
elif marks > 70 and marks < 80:
    print("Grade: A")
else:
    print("Need more improvement.")

# Loops
for i in range(10):
    print(i)

    