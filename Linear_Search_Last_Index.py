numbers = [10, 20, 30, 40]
target = 25

last_index = -1

for i, num in enumerate(numbers):
    if num == target:
       last_index = i
       break

if last_index == -1:
    print("Not Found")
else:
    print(last_index)