# Q 2566
max_num = 0
A = []

for i in range(9):
    A.append(list(map(int, input().split())))
    max_a = max(A[i])
    index_i = A[i].index(max_a) + 1
    
    if max_a > max_num:
        max_num = max_a
        index_v = i+1
        index_h = index_i
    else:
        continue
    
print(max_num)
print(index_v, index_h)
