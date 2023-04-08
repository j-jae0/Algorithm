a, b = map(int, input().strip().split(' '))
s = ''
for _ in range(b):
    s += '*'*a + '\n'

print(s)