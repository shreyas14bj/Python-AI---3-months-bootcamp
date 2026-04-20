import csv

data = [
    ["Name", "Department", "Salary"],
    ["Shreyas", "IT", "50000"],
    ["Rahul", "HR", "30000"],
    ["Anita", "IT", "70000"],
    ["Kiran", "Finance", ""],   # Missing salary (real-world issue)
    ["Meena", "IT", "60000"]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("employees.csv created")

# Clean and convert data
cleaned_data = []
with open("employees.csv", "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    # for row in reader:
    #     print(row)
    for row in reader:
        name = row["Name"]
        dept = row["Department"]
        salary = row["Salary"]

        if salary == "":
            salary = 0
        else:
            salary = int(salary)

        cleaned_data.append({
            "Name" : name,
            "Department" : dept,
            "salary" : salary
        })
print(cleaned_data)
    

