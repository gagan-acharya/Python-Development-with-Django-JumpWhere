str = "The quick brown fox jumps over the lazy dog."
n = 5
modified_str = ''

for char in range(0, len(str)):

	if(char != n):
		modified_str += str[char]

print("Modified string after removing ", n, "th character is: ")
print(modified_str)