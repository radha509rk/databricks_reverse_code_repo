def reverse_number(n):
    rev = 0
    num = abs(n)
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return -rev if n < 0 else rev
original = 12345
reversed_num = reverse_number(original)
print("Original:", original)
print("Reversed:", reversed_num)