# Create input file
data_lines = [
    "Shreyas, 90",
    "Sneha, 95",
    "Manoj, 94",
    "Deepu, 92"
]

with open("student_data.txt", "w") as file:
    for line in data_lines:
        file.write(line + "\n")
print("File created successfully and written the data into it...")

# Function to assign grade
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"
    
# Read and Process data
with open("student_data.txt", "r") as file:
    data = file.readlines()

with open("output.txt", "w") as file:
    for line in data:
        clean = line.strip()

        # Skip empty lines
        if clean == "":
            continue

        name, marks = clean.split(",")
        marks = int(marks)

        grade = get_grade(marks)
        file.write(f"{name} - {marks} - {grade}\n")
print("Processing completed. Check 'output.txt'")