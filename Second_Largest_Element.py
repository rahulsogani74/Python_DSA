numbers = [-10, -5, -20, -3]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        largest, second_largest = num, largest
    elif num < largest and num > second_largest:
        second_largest = num
    
if second_largest == float('-inf'):
    print("Second Largest does not exist")
else:   
    print("Second Largest:", second_largest)