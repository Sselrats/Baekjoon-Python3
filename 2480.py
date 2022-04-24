a = [0 for i in range(10)]
b = list(map(int, input().split()))
for i in range(3):
    a[b[i]] += 1
chk = 0
for i in range(7):
    if a[i]==3:
        print(10000+1000*i)
        exit()
    elif a[i]==2:
        print(1000+100*i)
        exit()
    elif a[i]==1:
        if chk == 2:
            print(i*100)
            exit()
        else:
            chk += 1
