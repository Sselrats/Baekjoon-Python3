a = input()
b = input()
a = int(a)
b = int(b)
d = a*(b%10)
e = a*((b//10)%10)
f = a*(b//100)
g = a*b
print(d, e, f, g, sep='\n')
