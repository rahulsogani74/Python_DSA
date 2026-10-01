numbers = [10, 25, 7, 42, 18]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        smallest, second_smallest = num, smallest
    elif num > smallest and num < second_smallest:
        second_smallest = num
    
if second_smallest == float('inf'):
    print("Second smallest does not exist")
else:   
    print("Second smallest:", second_smallest)