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

# Q 1152
import sys
S = list(map(str, sys.stdin.readline().split()))
print(len(S))

# Q 2908
a, b = map(str, input().split())

def reverse(sample_string):
    rev_score = 0
    
    for i in range(3):
        rev_score += (10**i) * int(sample_string[i])
    
    return rev_score

A = reverse(a)
B = reverse(b)

print(max(A,B))

# Q 2675
N = int(input())
for i in range(N):
    a, b = map(str, input().split())
    
    for j in range(len(b)):
        for k in range(int(a)):
            print(b[j], end="")
    
    print("")

# Q 5622
answer_dic = {'A':3, 'B':3, 'C':3, 'D':4, 'E':4, 'F':4, 'G':5, 'H':5, 'I':5, 'J':6, 'K':6, 'L':6, 
              'M':7, 'N':7, 'O':7, 'P':8, 'Q':8, 'R':8, 'S':8, 'T':9, 'U':9, 'V':9, 'W':10, 'X':10, 'Y':10, 'Z':10}

ST = str(input())
score = 0

for i in range(len(ST)):
    score += answer_dic[ST[i]]

print(score)
'''

# Q 11718
while True:
    line = str(input())
    if line == "":
        break
    print(line)