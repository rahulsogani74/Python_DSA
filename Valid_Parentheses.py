def isValid(s):
    stack = []
    
    pairs = {')' : '(', '}' : '{', ']' : '['}
    
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
            
    return len(stack) == 0

s = "({[]})"

result = isValid(s)
if result:
    print("The parentheses are valid.")
