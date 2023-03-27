def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "TestString"
print(findLen(str))