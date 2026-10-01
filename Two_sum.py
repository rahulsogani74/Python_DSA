numbers = [3, 8, 12, 4, 7]
target = 11

seen = {}

for i, num in enumerate(numbers):
    complement = target - num
    
    if complement in seen:
        print([seen[complement], i])
        break
    else:
        seen[num] = i