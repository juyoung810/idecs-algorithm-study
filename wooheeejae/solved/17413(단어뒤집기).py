 # 기본 변수 설정
S = list(input())
tempList = []
ansList = []

 # 문제 풀이
 # 뒤집지않는 경우
def fun1():
    for i in range(len(S)):
        if S[i] == '>':
            # <~>를 temp에 옮김
            tempList.append(S[0:(i+1)])
            del S[:(i+1)]
            break
 # 뒤집는 경우
def fun2():
    for i in range(len(S)):
        # <나 띄어쓰기를 만나면 그 전까지를 뒤집어서 tmep에 옮김
        if (S[i] == '<') or (S[i] == " "):
            tempList.append(S[(i-1)::-1])
            del S[:(i)]
            break
        # 끝까지 <나 띄어쓰기가 없을 때
        if i == (len(S)-1):
            tempList.append(S[(i)::-1])
            del S[:(i+1)]
            break

while len(S) > 0:
     if S[0] == '<':
         fun1()
     elif S[0] == ' ':
         tempList.append(S[0])
         del S[0]
     else:
         fun2()

for i in tempList:
    ansList += i
answer = ''.join(ansList)

print(answer)