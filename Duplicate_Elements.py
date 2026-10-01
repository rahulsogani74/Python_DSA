numbers = [5, 7, 5, 2, 9, 7, 5, 2, 8]

seen = set()
duplicates = []

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else :
        seen.add(num)
        
print(duplicates)