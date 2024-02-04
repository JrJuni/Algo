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
    
    print(str(fl)+ho_str)

# Q 2941
S = str(input())
position = 0
cnt = 0

while position < len(S):
    if position == len(S)-1 :
        cnt += 1
        position += 1
        break
    
    elif S[position] == 'c':
        if S[position+1] == '-':
            cnt += 1
            position += 2
        elif S[position+1] == '=':
            cnt += 1
            position += 2
        else:
            cnt += 1
            position += 1
            
    elif S[position] == 'd':
        if S[position+1] == '-':
            cnt += 1
            position += 2
        elif (S[position+1] == 'z'):
            if position == len(S)-2 :
                cnt += 2
                position += 2
            elif (S[position+2] == "="):
                cnt += 1
                position += 3
            else:
                cnt += 1
                position += 1
        else:
            cnt += 1
            position += 1
            
    elif S[position] == 'l':
        if S[position+1] == 'j':
            cnt += 1
            position += 2
        else:
            cnt += 1
            position += 1    

    elif S[position] == 'n':
        if S[position+1] == 'j':
            cnt += 1
            position += 2
        else:
            cnt += 1
            position += 1  

    elif S[position] == 's':
        if S[position+1] == '=':
            cnt += 1
            position += 2
        else:
            cnt += 1
            position += 1  

    elif S[position] == 'z':
        if S[position+1] == '=':
            cnt += 1
            position += 2
        else:
            cnt += 1
            position += 1                        
    else:
        cnt += 1
        position += 1

print(cnt)

# 파이썬의 re 라이브러리는 정규 표현식(Regular Expression)을 활용하여 문자열 패턴을 검색, 추출, 대체하는 기능을 제공하는 라이브러리입니다.

re 라이브러리의 주요 함수와 메서드 몇 가지를 살펴보겠습니다:
1. re.search(pattern, string): 주어진 문자열에서 정규 표현식 패턴에 매치되는 첫 번째 부분 문자열을 검색합니다.
2. re.match(pattern, string): 주어진 문자열의 시작 부분에서 정규 표현식 패턴에 매치되는지 확인합니다.
3. re.findall(pattern, string): 주어진 문자열에서 정규 표현식 패턴에 매치되는 모든 부분 문자열을 찾아 리스트로 반환합니다.
4. re.sub(pattern, repl, string): 주어진 문자열에서 정규 표현식 패턴과 일치하는 부분을 다른 문자열로 대체합니다.

''' 

