a = int(input().rstrip(), 16)
for i in range(1, 16):
    print('%X*%X=%X' % (a, i, a*i))

# https://stackoverflow.com/questions/20450531/python-operator-in-print-statement

num = int(input(), 16)
for i in range(1, 16):
    print(f'{num:X}*{i:X}={num * i:X}')
