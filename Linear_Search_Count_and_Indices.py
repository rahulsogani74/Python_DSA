numbers = [5, 2, 7, 2, 9, 2]
target = 2

count = 0
indices = []

for i, num in enumerate(numbers):
    if num == target:
        count += 1
        indices.append(i)
        
print(count)
print(indices)