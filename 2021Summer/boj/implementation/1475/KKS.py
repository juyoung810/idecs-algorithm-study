n = input()
data = []
for i in range(9+1):
    data.append(int(n.count(str(i)))) #인덱스에 해당하는 숫자의 갯수를 카운팅해서 배열에 입력
max_value = max(data) #가장 많이 나온 횟수 확인
max_idx = data.index(max_value) #가장 많이 나온 횟수의 인덱스 찾기/ 인덱스가 곧 숫자이다
if max_idx == 6 or max_idx ==9: # 만약에 가장 많이 등장하는 숫자가 6이나 9일때
    if (data[6] + data[9])%2 == 0: # 6과9의 합을 2로 나눴을때 나머지 0이면
        print((data[6] + data[9])//2) #몫을 출력하고
    else: #나머지가 0이 아니면
        print(((data[6] + data[9]) // 2)+1) #몫 + 1을 출력
else: #가장 많이 등장하는수가 6이나 9가 아니면
    print(max_value) #그 수의 등장횟수를 출력