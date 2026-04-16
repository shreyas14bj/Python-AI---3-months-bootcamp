students = {
    "Shreyas" : [80, 90, 70],
    "Sneha" : [90, 95, 98]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name} : Average: {avg}")

    if avg >= 90:
        print("Grade A+")
    elif avg >= 75:
        print ("Grade A")
    else:
        print("Grade B")
