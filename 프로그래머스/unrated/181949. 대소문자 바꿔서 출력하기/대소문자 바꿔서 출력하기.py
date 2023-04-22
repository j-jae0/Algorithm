str = input()
new_str = ''
for s in str:
    if s in 'abcdefghijklmnopqrstuvwxyz':
        new_str += s.upper()
    else:
        new_str += s.lower()
print(new_str)