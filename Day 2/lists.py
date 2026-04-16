marks = [80, 90, 70, 60]
print(marks[0]) # print 0th index element
print(marks[1]) # print 1st index element
print(marks[2]) # print 2nd index element
print(marks[-1]) # print last element

# Print all marks using loop
for i in marks:
    print(i, end = " ")

# # Lists are dynamic ordered and mutable

numbers = [10,20,30,40]
names = ["Shreyas", "Sneha", "Manoj", "Deepu"]

print(numbers[0])
print(names[-1])

# modifying
numbers[1] = 25
print(numbers) 

# adding
numbers.append(50)  #add at the end
numbers.insert(1, 20)  #insert at position
print(numbers)

# removing
numbers.remove(30)  #removes
numbers.pop()  #remove last element
numbers.pop(1)  #remove element at index 1
print(numbers)

# to print lst length
print(len(numbers))

# looping
for num in numbers:
    print(num)

# sorting
names.sort()
print(names)

# reversing
names.reverse()
print(names)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

# slicing
print(numbers[1:4])
print(numbers[:3])  #first 3
print(numbers[2:])  #from 2 to end

# list stores multiple values in order and allows modifications
num = [1,3,45,6,78,9,5]
names = ['A', 'B', 'C', 'E', 'G', 'A', 'D']
mix = [1, 'A', 3.14, True]

print(mix)

num.extend([60, 70])
print(num)

del num[0]
print(num)

# list
marks = [85, 90, 78, 92]

# Access
print(marks[0])

# Modify
marks[0] = 100
print(marks[0])

# Add
marks.append(95)
print(marks)

# Remove
marks.remove(78)
print(marks)

# Length
print(len(marks))

# Core concepts
# 1. Add data - append()
# 2. Remove data - remove()
# 3. Access by index
# 4. Loop through data

# creating list
sales = [1200, 3400, 2800, 4000]

# add new value
sales.append(5000)
print(sales)

# total sales
print(sum(sales))

# average
print(sum(sales) / len(sales))