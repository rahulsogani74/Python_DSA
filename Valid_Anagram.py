import array

s = "anagram"
t = "nagaram"

arr = array.array('i', [0] * 26)

for i in range(len(s)):
    arr[ord(s[i]) - ord('a')] += 1
    arr[ord(t[i]) - ord('a')] -= 1
    
for i in range(len(arr)):
    if arr[i] != 0:
        print("Not an Anagram")
        break
else:
    print("Anagram")
    