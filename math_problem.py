'''
# Q 1978
N = int(input())

prime = [1] * 1001
prime[0] = 0
prime[1] = 0

def nonprime_killer (sample_list, denom):
    for i in range(1, 1000//denom):
        sample_list[denom*(i+1)] = 0
        
for j in range(2, 500):
    nonprime_killer (prime, j)

q_num = list(map(int, input().split()))
cnt = 0

for k in range(N):
    if prime[q_num[k]] == 1:
        cnt += 1
    else:
        continue

print(cnt)

# all 함수를 쓰면 더 간단히 정리할 수 있다.
all은 하나라도 False가 있다면 False를 반환한다.

'''
# Q 2609
a, b = map(int, input().split())
min = 1
for i in range(2, 100):
    while True:
        if a%i == 0:
            if b%i == 0:
                a = a//i
                b = b//i
                min *= i

            else:
                break
        
        else:
            break
        
print(min)
print(min*a*b)            
    

