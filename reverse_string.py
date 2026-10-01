def reverse_string(text: str) -> str :
    stack = []
    
    for ch in text:
        stack.append(ch)
        
    reverse_text = ""
    
    while len(stack) > 0 :
        reverse_text += stack.pop()
        
    return reverse_text
    
print(reverse_string("hello"))