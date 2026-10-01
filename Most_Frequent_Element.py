numbers = [5, 2, 5, 8, 2, 5, 9, 8, 2]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

most_frequent = []
max_count = 0

for num, count in frequency.items():
    if count > max_count:
        most_frequent.clear()
        max_count = count
        most_frequent.append(num)
    elif count == max_count:
        most_frequent.append(num)
    
        
# print(frequency)
print(most_frequent)