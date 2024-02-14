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
# Q 2231
def gen_num(x):
    if x > 9:
        stx = str(x)
        gen = x
        for k in range(len(stx)):
            gen += int(stx[k])
    else:
        gen = 2*x
        
    return gen

N = int(input())
num = len(str(N))

final_gen = N-1
i = 0
answer = 0

while i < num*9:
    if gen_num(final_gen) == N:
        answer = final_gen
    else:
        pass
    
    final_gen -= 1
    i += 1
    
print(answer)