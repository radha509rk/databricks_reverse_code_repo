def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True 
input_str = "racecar"
print("ORIGINAL_STRING:",input_str)
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not Palindrome")