import sys
input = sys.stdin.readline

S = input().rstrip()
inner = False
word = ''
result = ''

for i in S:
    if inner == False: # < > 외부
        if i == '<':
            inner = True
            result += word
            result += i
            word = ''
        elif i == ' ':
            word += i
            result += word
            word = ''
        # elif i == '>': 는 나올수 없는 경우
        else:
            word = i + word 
    else: # < > 내부
        if i == '>':
            result += i
            inner = False
        else:
            result += i
if len(word) >0:
    result += word
print(result)



############################################
# 출처 : https://jeongm1n.tistory.com/
# import sys
# input = sys.stdin.readline

# s = input().rstrip()
# flag = False
# word = ""
# answer = ""

# for i in s:
#     if flag == False:
#         if i == "<":
#             flag = True
#             word += i
#         elif i == " ":
#             word += i
#             answer += word
#             word = ""
#         else:
#             word = i + word

#     else:
#         word += i
#         if i == ">":
#             flag = False
#             answer += word
#             word = ""

# print(answer + word)


############################################
# 시도 중
# import sys
# input = sys.stdin.readline

# S = '-' + input().strip() + '-'
# S = S.replace('<', '-<-')
# S = S.replace('>', '->-')

# word_list = S.split('-')
# result = []
# for i in range(len(word_list)):
#     if word_list[i] == '<':
#         x = word_list[i-1].split()
#         for j in range(len(x)):
            
#         result.append(x)
#     else:
#         result.append(word_list[i-1])
# print(result)