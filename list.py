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
'''

# Q 10871
import sys
N, X = map(int, sys.stdin.readline().split())
q_list = list(map(int, sys.stdin.readline().split()))
a_list = []

for i in range(N):
    if q_list[i] < X:
        a_list.append(q_list[i])

print(a_list)

final = map(str, a_list)
final = ' '.join(final)
print(final)
