numbers = [10, 25, 7, 42, 18]

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

    if num > maximum:
        maximum = num

print("Min:", minimum)
print("Max:", maximum)