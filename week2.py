import random

# Generate a list of 10 random integers between 1 and 100
numbers = [random.randint(1, 100) for i in range(10)]
print("Randomly generated list of integers:", numbers)

# Find the sum of all elements in the list
sum_of_numbers = sum(numbers)
print("Sum of all elements in the list:", sum_of_numbers)

