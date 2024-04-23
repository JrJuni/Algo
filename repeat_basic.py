'''
# Q 2739
n = int(input())
for i in range(1,10):
    multi = n*i
    print(f'{n} * {i} = {multi}')

# Q 10950
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)

# Q 8393 - 이게 반복으로 풀 일인가...
n = int(input())
print(n*(n+1)//2)

# Q 25405 Receipt
import sys
receipt_price = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total_price = 0

for i in range(n):
    price, num = map(int, sys.stdin.readline().split())
    total_price += (price*num)

if receipt_price == total_price:
    print("Yes")
else:
    print("No")

# Q 25314
n = int(input())
for i in range(n//4):
    print("long", end=" ")
print("int")

# Q 15552
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    
# Q 11021
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')
    
# Q 11022
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
    
# Q 2438
import sys
n = int(sys.stdin.readline().rstrip())
a = ""

for i in range(n):
    a += "*"
    print(a)   
     
# Q 2439
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a = ""
    a += " "*(n-i-1)
    a += "*"*(i+1)
    print(a) 

# Q 10952
while(1):
    a, b = map(int, input().split())
    if a==0 & b==0:
        break
    else:
        print(a+b)
        
# Q 10951
import sys

while(1):
    try:
        a, b = map(int, sys.stdin.readline().split())
    except:
        break
    
    if a==0 & b==0:
        break
    else:
        print(a+b)
'''

# Q 1316
alpha = []
for i in range(97,123):
    alpha.append(chr(i))

N = int(input())
cnt = 0

for j in range(N):
    target_word = str(input())
    
    for k in alpha:
        temp_word = 0
        
        for scanner in range(len(target_word)):
            
            if k == target_word[scanner]:
                if temp_word == 0:
                    temp_word = 1
                elif k == target_word[scanner-1]:
                    continue
                else:
                    temp_word = 2
                    break
            else:
                continue
        
        if temp_word == 2:
            break
        else:
            continue
        
    if temp_word == 2:
        continue
    else:
        cnt+=1
            
print(cnt)