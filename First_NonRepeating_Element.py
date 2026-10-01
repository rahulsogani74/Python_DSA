numbers = [4, 5, 1, 2, 1, 5, 4, 9]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num in numbers:
    if frequency[num] == 1:
        print(num)
        break
