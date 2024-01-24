'''
# Q 27866
S = str(input())
n = int(input())
print(S[n-1])

# Q 2743
S = str(input())
print(len(S))

# Q 9068
def first_end(s):
    print(s[0],end="")
    print(s[-1])

N = int(input())

for i in range(N):
    first_end(str(input()))

# Q 11654
c = str(input())
ascii_value = ord(c)
print(ascii_value)

# Q 11720

N = int(input())
S = str(input())

sum_str = 0
for i in range(N):
    sum_str += int(S[i])
    
print(sum_str)

# Q 10809
def list_crack(cracktarget):
    crack_ver = map(str, cracktarget)
    crack_ver = ' '.join(crack_ver)
    print(crack_ver)

letter_score = [-1]*26

S = str(input())

for i in range(len(S)):
    temp_letter = ord(S[i]) - 97
    if letter_score[temp_letter] == -1:
        letter_score[temp_letter] = i
    else:
        continue
    
list_crack(letter_score)
'''
# Q 1152
import sys
S = list(map(str, sys.stdin.readline().split()))
print(len(S))



