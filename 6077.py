n = int(input().rstrip())
m = 0
for i in range(1, n+1):
    if i % 2 == 0:
        m += i

print(m)
