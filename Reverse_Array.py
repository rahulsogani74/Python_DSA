numbers = [10, 20, 30, 40, 50]

# reversed_numbers = []

# last_index = len(numbers) - 1

# for i in numbers:
#     if last_index != -1 :
#         reversed_numbers.append(numbers[last_index])
#         last_index -= 1
        
# print("Reversed Array:", reversed_numbers)

left = 0
right = len(numbers) - 1

while right > left:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    
    left += 1
    right -= 1
    
print("Reversed Array:", numbers)