'''# Q 25083
st_list = ["a","a","a","a","a","a"]

st_list[0] ="         ,r'\"7"
st_list[1] ="r`-_   ,'  ,/"
st_list[2] =" \\. \". L_r'"
st_list[3] ="   `~\\/"
st_list[4] ="      |"
st_list[5] ="      |"

for i in range(6):
    print(st_list[i])
# Q 2444
N = int(input())

for i in range(N-1):
    blank = " "*(N-1-i)
    star = "*"*(2*i+1)
    print(blank, end="")
    print(star)
    
center_star = "*"*(2*N-1)
print(center_star)

for i in range(N-1):
    blank = " "*(i+1)
    star = "*"*(2*(N-i)-3)
    print(blank, end="")
    print(star)
''' 

# Q 10250
T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    
    ho = ((n-1) // h) + 1
    fl = n % h

    if fl == 0:
        fl = h
    else:
        pass
  
    if ho < 10:
        ho_str = "0"+str(ho)
        
    else:
        ho_str = str(ho)
    
    print(str(fl))
    print(str(fl)+ho_str)
    
