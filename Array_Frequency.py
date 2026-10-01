numbers = [4, 7, 4, 2, 7, 4, 9]

frequency = {}

for num in numbers:
    # if num in frequency :
    #     frequency[num] += 1
    # else :
    #     frequency[num] = 1
    frequency[num] = frequency.get(num, 0) + 1
        
print(frequency)