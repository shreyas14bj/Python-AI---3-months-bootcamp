data = [10, 20, None, 40, None, 50]
cleaned = []
for i in data:
    if i is not None:
        cleaned.append(i)
print(cleaned)
total = sum(cleaned)
print(total)