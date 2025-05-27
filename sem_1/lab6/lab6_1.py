from itertools import product
count = 0
for x in product ('тимофей', repeat = 5):
    s = ''.join(x)
    if s.count('й') <= 1 and 'йи' not in s and 'ий' not in s and s[0] != 'й' and s[1:] != 'й':
        count += 1
print(count)
