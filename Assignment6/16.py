lists=[]
n=int(input('Enter the no. of elements: '))
for i in range(n):
    ele=int(input(''))
    lists.append(ele)
find=int(input("Enter the element to be deleted: "))
if find in lists:
    lists.remove(find)
print(lists)