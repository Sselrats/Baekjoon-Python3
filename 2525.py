h, m = map(int, input().split())
d = int(input())

a = h*60 + m + d

print(a%1440//60, a%1440%60)
