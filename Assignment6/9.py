qty=int(input('Enter quantity: '))
cost = (qty * 100)
if cost >= 1000:
    print('You got discount of 10% on purchasing of :', cost)
    discount = cost * (10 / 100)
    print("Your discount is ", discount)
    price = cost - discount
    print('You have to pay only ', price)
else:
    print("You have to pay : ", cost)
