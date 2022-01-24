 # 기본 변수 설정
text = 0
temp = []

 # 문제 풀이
while text != '*':
     text = str(input())
     for i in range(len(text)):
          if 1 in temp:
               continue
          for j in range(len(text)):
               if 1 in temp:
                    continue
               D = text[j:(j+i+2):(i+1)]
               if len(D) == 2:
                    if D not in temp:
                         temp.append(text[j:(j+i+2):(i+1)])
                    else:
                         temp.append(1)
                         continue
          if 1 not in temp:
               temp = []
     if 1 in temp:
          print(f"{text} is NOT surprising.")
     else:
          print(f"{text} is surprising.")
     temp = []




