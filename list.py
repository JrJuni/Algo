'''
# Q 10807
import sys

N = int(sys.stdin.readline())
q_list = list(map(int, sys.stdin.readline().split()))
a_list = [0]*220

for i in range(N):
    a_list[q_list[i]]+=1

index = int(input())
print(a_list[index])

# Q 10871
import sys
N, X = map(int, sys.stdin.readline().split())
q_list = list(map(int, sys.stdin.readline().split()))
a_list = []

for i in range(N):
    if q_list[i] < X:
        a_list.append(q_list[i])

final = map(str, a_list)
final = ' '.join(final)
print(final)

# Q 10818
import sys
N = int(sys.stdin.readline())
q_list = list(map(int, sys.stdin.readline().split()))
q_minmax = [q_list[0], q_list[0]]

for i in range(N):
    if q_list[i] < q_minmax[0]:
        q_minmax[0] = q_list[i]
    elif q_list[i] > q_minmax[1]:
        q_minmax[1] = q_list[i]
    else:
        continue
    
print(q_minmax[0], end=" ")
print(q_minmax[1])

# max_val = max(q_list)
# min_val = min(q_list)

# Q 3003
import sys
ori_chess = [1, 1, 2, 2, 2, 8]
input_chess = list(map(int, sys.stdin.readline().split()))

for i in range(6):
    if i == 5:
        print(ori_chess[i]-input_chess[i])
    else:
        print(ori_chess[i]-input_chess[i], end=" ")
# Q 25206
import sys
total_score = 0
total_class = 0
q_dict ={"A+": 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0 }

for i in range(20):
    class_name, cl, sc = map(str, sys.stdin.readline().split())
    if sc == "P":
        continue
    else:
        cl = int(float(cl))
        total_class += cl
        total_score += (q_dict[sc]*cl)
    
print(total_score/total_class)

# Q 2562
import sys
n, m = map(int, sys.stdin.readline().split())

def put_ball(i, j, k, target_list):
    for x in range(i-1, j):
        target_list[x] = k
        
def list_crack(cracktarget):
    crack_ver = map(str, cracktarget)
    crack_ver = ' '.join(crack_ver)
    print(crack_ver)
        
final_list = [0]*n

for y in range(m):
    i_input, j_input, k_input = map(int, sys.stdin.readline().split())
    put_ball(i_input, j_input, k_input, final_list)
   
list_crack(final_list)

# Q 10813
import sys
n, m = map(int, sys.stdin.readline().split())

def trade_ball(i, j, target_list):
    target_list[i-1], target_list[j-1] = target_list[j-1], target_list[i-1] 
        
def list_crack(cracktarget):
    crack_ver = map(str, cracktarget)
    crack_ver = ' '.join(crack_ver)
    print(crack_ver)
        
final_list = [gen_i for gen_i in range(1, n+1)]

for y in range(m):
    i_input, j_input = map(int, sys.stdin.readline().split())
    trade_ball(i_input, j_input, final_list)
   
list_crack(final_list)

# Q 5597
class_no = [0]*30

for i in range(28):
    st_no = int(input())
    class_no[st_no-1] = 1

for j in range(30):
    if class_no[j] == 0:
        print(j+1)

# Q 3052
modi = [0]*43

for i in range(10) :
    mo = int(input())
    mo = mo % 42
    modi[mo] = 1

print(sum(modi))

# Q 1546
import sys
N = int(input())

score = list(map(float, sys.stdin.readline().split()))
max_sc = max(score)

for i in range((len(score))):
    score[i] = (score[i]*100)/max_sc
    
average_sc = sum(score) / len(score)
print(average_sc)

# Q 10811
N, M = map(int, input().split())
ori_list = [i for i in range(1, N+1)]

def shake(a, b, list_name):
    while a < b:
        list_name[a-1],list_name[b-1] = list_name[b-1],list_name[a-1]
        a += 1
        b -= 1

def list_crack(cracktarget):
    crack_ver = map(str, cracktarget)
    crack_ver = ' '.join(crack_ver)
    print(crack_ver)
        

for i in range(M):
    i, j  = map(int, input().split())
    shake(i, j, ori_list)

list_crack(ori_list)

# Q 2738 - Numpy 수련법
import numpy as np
import sys

n, m = map(int, input().split())

M1 = np.zeros((n,m))
for i in range(n):
    M1[i] = list(map(int, sys.stdin.readline().split()))

M2 = np.zeros((n,m))
for j in range(n):
    M2[j] = list(map(int, sys.stdin.readline().split()))
    
result = np.add(M1, M2)

for i1 in range(n):
    for i2 in range(m):
        print(int(result[i1][i2]), end=" ")
    print("")
    
# Q 2738
import sys

n, m = map(int, input().split())

def mat(n1, m2):
    matric = [[]]*n1
    for i2 in range(n1):
        matric[i2] = list(map(int, sys.stdin.readline().split()))
    
    return matric

M1 = mat(n, m)
M2 = mat(n, m)

for i3 in range(n):
    for j3 in range(m):
        M1[i3][j3] += M2[i3][j3]

for i1 in range(n):
    for i2 in range(m):
        print(int(M1[i1][i2]), end=" ")
    print("")

import sys

ori = list(map(int, sys.stdin.readline().split()))
final = 0

for i in range(len(ori)):
    final += ori[i]**2

print(final%10)

# Q 1259
while True:
    S = str(input())
    if S =='0':
        break
    else:
        pass
    
    P = 0
    
    for i in range(len(S)//2 + 1):
        if S[i] == S[-1-i]:
            continue
        else:
            P = 1
    
    if P == 1:
        print("no")
    else:
        print("yes")

# 숏코딩
while int(s:=input()):print('yneos'[s!=s[::-1]::2])

":="는 파이썬 3.8 버전부터 도입된 할당 표현식입니다. 이는 대입 연산자로 사용되며, 변수에 값을 할당하고 동시에 해당 값을 반환합니다.
예를 들어, s := input()은 사용자로부터 입력을 받아 변수 s에 할당하는 동시에 s의 값을 반환합니다. 이는 기존에는 다음과 같이 두 줄로 나누어 작성해야 했던 코드를 간결하게 표현할 수 있도록 도와줍니다:
s = input()

'''

# Q 1102
print("s")