numbers = [10, 25, 7, 42, 25, 18]

seen = set()

for num in numbers:
    if num in seen:
        print("Duplicate:", num)
        break
    else:
        seen.add(num)
