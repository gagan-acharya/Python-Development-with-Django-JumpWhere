w=[2, 3.0,4.3,"hello world", 5, 4.3]
x=[]
y=[]
z=[]

for i in w:
    if type(i)==int:
        x.append(i)
    elif type(i)==float:
        y.append(i)
    elif type(i)==str:
        z.append(i)
print(x)
print(y)
print(z)