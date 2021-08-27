# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리.

# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
# ex) 리스트['a','b','c']에서 3개를 뽑아 나열하는 모든 경우를 출력하는 예시
from itertools import permutations

data = ['A','B','C']    # 데이터 준비
result = list(permutations(data, 3))    # 모든 순열 구하기

print(result)


# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
# ex) 리스트 ['A','B','C']에서 2개를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력하는 예시
from itertools import combinations

data = ['A','B','C']    # 데이터 준비
result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합 구하기

print(result)


# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산한다. 원소 중복해서 뽑는다.
# ex) 리스트 ['A','B','C']에서 중복을 포함하여 2개를 뽑아 나열하는 모든 경우를 출력하는 예시
from itertools import product

data = ['A','B','C']    # 데이터 준비
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)


# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 원소 중복해서 뽑는다.
# ex) 리스트 ['A','B','C']에서 중복을 포함하여 2개를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력하는 예시
from itertools import combinations_with_replacement

data = ['A','B','C']    # 데이터 준비
result = list(combinations_with_replacement(data, 2))   # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result)