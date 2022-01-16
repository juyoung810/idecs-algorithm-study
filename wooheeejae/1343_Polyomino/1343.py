#폴리오미노
 # 기본 변수 설정
poly = str(input())

 # 문제 풀이
 # XXXX인 경우 먼저 AAAA로 바꿈
poly = poly.replace("XXXX", "AAAA")
 # 남은 XX들을 BB로 바꿈
poly = poly.replace("XX", "BB")

 # X가 남아있는 경우
if "X" in poly:
    print(-1)
 # 위에서 정리가 다 된 경우
else:
    print(poly)
