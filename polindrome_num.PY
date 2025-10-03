def is_palindrome_number(junnu):
    original_num = junnu
    reversed_num = 0

    num = junnu   
    while num > 0:

        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    if original_num == reversed_num:
        return True
    else:
        return False

input = 12321
final_ans = is_palindrome_number(input)
print("ORIGINAL_NUMBER:",input)
print(final_ans)
if final_ans:
    print("Palindrome")
else:
    print("Not Palindrome")