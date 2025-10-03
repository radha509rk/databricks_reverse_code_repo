def reverse_string(input_str):
    reversed_str =""
    i = len(input_str) - 1
    while i >= 0:
        reversed_str += input_str[i]
        i -= 1
    return reversed_str
input_str = "MADAM"
result = reverse_string(input_str)
print("ORIGINAL_STRING:",input_str)
print("REVERSED_STRING:",result)