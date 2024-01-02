'''
# Q 2739
n = int(input())
for i in range(1,10):
    multi = n*i
    print(f'{n} * {i} = {multi}')
'''

# Q 10950
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)