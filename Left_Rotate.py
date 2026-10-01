def reverse(numbers, left, right):
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
        
def left_rotaion(numbers, k):
    reverse(numbers, 0, k-1)
    reverse(numbers, k, len(numbers)-1)
    reverse(numbers, 0, len(numbers)-1)
    
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
left_rotaion(numbers, 3)
    
print(numbers)