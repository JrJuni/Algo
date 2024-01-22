'''
# Q 27866
S = str(input())
n = int(input())
print(S[n-1])

# Q 2743
S = str(input())
print(len(S))
'''


# Q 9068
def first_end(s):
    print(s[0],end=" ")
    print(s[-1])

N = int(input())

for i in range(N):
    first_end(str(input()))