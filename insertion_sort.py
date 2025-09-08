import random

sorted_numbers = []
unsorted_numbers = []

# generating unsorted numbers in the following 2 lines
for i in range(100):
    unsorted_numbers.append(random.randint(-1000, 1000))

print("unsorted_list=", unsorted_numbers)

# the bigger "for" is used to sort numbers
for number in unsorted_numbers:
    for index in range(len(sorted_numbers)):
        if sorted_numbers[index] > number:
            sorted_numbers.insert(index, number)
            break
    else:
        sorted_numbers.append(number)

print("sorted_list=", sorted_numbers)
