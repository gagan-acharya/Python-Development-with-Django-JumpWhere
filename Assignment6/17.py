def func(x, y):
	prime_list = []
	even_list = []
	odd_list = []
	for i in range(x, y):
		if i == 0:
			continue
		if i == 1:
			odd_list.append(i)
			continue
		else:
			if i%2==0:
				even_list.append(i)
			else:
				odd_list.append(i)
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return even_list,odd_list,prime_list
starting_range = 1
ending_range = 101
elst,olst,plst = func(starting_range, ending_range)
if len(elst) == 0:
	print("There are no even numbers in this range")
else:
	print("The even numbers in this range are: ", elst)
if len(olst) == 0:
	print("There are no odd numbers in this range")
else:
	print("The odd numbers in this range are: ", olst)
if len(plst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", plst)