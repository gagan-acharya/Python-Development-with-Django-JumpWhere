count = 0 
sum = 0 
product = 1 
while True:
    user_input = input('Enter a number: ')
    if (user_input =="q" ):
        break
    user_input = int(user_input)
    sum = sum + user_input
    product = product * user_input
    count = count + 1
print('Average:', sum/count)
print('Product:', product)