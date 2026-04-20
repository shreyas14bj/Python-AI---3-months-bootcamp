with open("data.txt", "w") as file:
    file.write("This is line 1\n")


with open("data.txt", "a") as file:
    file.write("\nThis is line 2")


with open("data.txt", "r") as file:
    data = file.readlines()
print(data)

# Cleaned data

with open("data.txt", "r") as file:
    data = file.readlines()
    for line in data:
        clean = line.strip()
        print(clean)

# Convert text to usable data
try:
    with open("data.txt" "r") as file:
        data = file.readlines()
        for line in data:
            clean = line.strip()
            print(clean)
            name, marks = clean.split(",")
            marks = int(marks)
            if marks >= 75:
                print("Pass")
            else:
                print("Fail")
except FileNotFoundError:
    print("The file you are looking is not found...")
