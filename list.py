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
'''

# Q 2562
    
        
