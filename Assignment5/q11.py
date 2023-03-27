def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('Keep'))
print(reverse_string('working'))
print(reverse_string('hard'))