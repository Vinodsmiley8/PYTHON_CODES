# Find the second-largest number in a list
numbers = [3, 7, 1, 5, 8, 2]
second_largest = sorted(set(numbers))[-2]
print("Second largest:", second_largest)