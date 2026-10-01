numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# right rotate by 1

# last_index = len(numbers) -1

# last_num = numbers.pop(last_index)
# numbers.insert(0, last_num)
    
# print(numbers)



# k = 2   # right rotate by k

# for i in range(k):
#     last_num = numbers.pop()
#     numbers.insert(0, last_num)

# print(numbers)  



def reverse(numbers, left, right):
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

def rotate_right(numbers, k):
    if not numbers:
        return

    k %= len(numbers)

    reverse(numbers, 0, len(numbers) - 1)
    reverse(numbers, 0, k - 1)
    reverse(numbers, k, len(numbers) - 1)
    

rotate_right(numbers, 3)

print(numbers)