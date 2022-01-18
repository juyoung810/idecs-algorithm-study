import sys
input = sys.stdin.readline

arr = list(input())


word = []
isTag = False
for s in arr:
    if s == '\n': break
    if s == "<": # 태그 시작
        if len(word) != 0: # 시작할 때 비어있지 않으면 그 이전은 word 이므로 역 출력
            word.reverse()
            print(''.join(word), end="")
            word =[]
        isTag = True # 태그 시작 더해줌
        word.append(s)
    elif s == ">": # 태그 끝
        word.append(s) # 태그 닫는 문자 더하기
        isTag = False
        print(''.join(word), end="") # 태그 그대로 출력
        word = []
    elif not isTag and s == " ": # 태그 아닌데 " "
        if len(word) != 0: # 태그 아니니까 word 끝난 경우
            word.reverse()
            print(''.join(word), end="") # 단어 뒤집어서 출력
            word = []
        if len(word) == 0: # 태그 내부 띄어쓰기 제외 출력
            print(" ", end = "")
    else:
        word.append(s)

word.reverse()
print(''.join(word), end="")


