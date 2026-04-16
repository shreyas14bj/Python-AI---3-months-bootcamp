# Reuse logic

def greet():
    print("hello")
greet()

# with parameter
def greet(name):
    print(f"Hello {name}, good morning💮")
greet("Shreyas")

# function to calculate average
def avg(data):
    return sum(data) / len(data)
average = avg([10, 20, 30])
print(average)