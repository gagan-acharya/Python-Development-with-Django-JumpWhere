intlist=[]
n=int(input("Enter no. of elements in list: "))
print('Enter elements: ')
for i in range(n):
    intlist.append(int(input()))
squarelist=[]
for i in intlist:
    squarelist.append(i*i)
print(squarelist)