a = [0 for i in range(2)]
for i in range(2):
    a[i] = int(input())
if a[0]>0:
    if a[1]>1:
        print(1)
    else:
        print(4)
else:
    if a[1]>1:
        print(2)
    else:
        print(3)
