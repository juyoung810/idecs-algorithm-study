 # 기본 변수 설정
poem = str(input())
space = int(input())
alpa = list(map(int, input().split()))
ansList = []

 # 문제 풀이
 # 연속된 문자, 띄어쓰기 삭제
for i in range(len(poem)-1):
    if poem[i] == poem[i+1]:
        poem = poem[:i] + "@" + poem[(i+1):]
poem = poem.replace("@","")

 # 띄어쓰기가 부족하면 탈락
if poem.count(" ") > space:
     print(-1)
     quit()

 # 알파벳이 부족하면 탈락
for i in range(0, 26):
    if (poem.count(chr(i+65)) + poem.count(chr(i+97))) > alpa[i]:
        print(-1)
        quit()

tempPoem = list(map(list, poem.split())) # 제목 출력위한 임시 리스트

 # 어절의 첫 글자만 따옴
for i in range(len(tempPoem)):
    ansList.append(tempPoem[i][0])

answer = (''.join(ansList)).upper() # 대문자 만들어주기

 # 내용과 제목을 합하여 부족하면 탈락
for i in range(0, 26):
    if ((poem+answer).count(chr(i+65)) + (poem+answer).count(chr(i+97))) > alpa[i]:
        print(-1)
        quit()

print(answer)