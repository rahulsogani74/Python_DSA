numbers = [7, 4, 9, 2, 5, 4, 8, 9]

seen = set()

for num in numbers:
    if num in seen:
        print(num)
        break
    else :
        seen.add(num)
        