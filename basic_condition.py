'''
# Q 1330
import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")
    
# Q 9498
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    
# Q 2753
year = int(input())

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("1")
        else:
            print("0")
    else:
        print("1")

else:
    print("0")
    
# Q 14681

x = int(input())
y = int(input())

multi = x*y
if multi > 0:
    if x > 0:
        print("1")
    else:
        print("3")
else:
    if x > 0:
        print("4")
    else:
        print("2")
        
# 문제 피드백
# 생각해보면 multiple 연산이 굳이 필요 없었다. 함수로 풀 거면 이산적 특성을 활용해야 했음.

리스트 슬라이싱을 활용한 간단한 코드가 있어 기록한다.
x = int(input())
y = int(input())
print("3421"[x>0::2][y>0])

# Q 2884
h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 23
    else:
        h = h-1
    
    m = m + 15
else:
    m = m - 45
    
print(h, m)
'''

# Q 2525
import sys
h, m = map(int, sys.stdin.readline().split())
clock = int(sys.stdin.readline())

h1 = clock//60
m1 = clock%60

m = m + m1
h = h + h1

if m >= 60:
    m = m - 60
    h = h + 1

h = h%24

print(h, m)