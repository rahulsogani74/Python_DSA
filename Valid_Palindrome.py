s = "A man, a plan, a canal: Panama"

clean_s = "".join(ch.lower() for ch in s if ch.isalnum() )

left = 0
right = len(clean_s)-1

is_Palindrome = True
    

while left < right:
    if clean_s[left] == clean_s[right]:
        left += 1
        right -= 1
    else:
        is_Palindrome = False
        break
        
print(is_Palindrome)