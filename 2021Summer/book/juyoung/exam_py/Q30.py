import sys

input = sys.stdin.readline

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????", "ke???"]

# words.sort()
# print(words)
# print(queries)
# answer = [0] * len(queries)
#
# for word in words:
#     print(word, end=": ")
#     for i in range(len(queries)):
#         query = queries[i]
#         if len(queries[i]) == len(word):
#             start = 0
#             end = len(queries[i]) - 1
#             state = True
#             while start <= end:
#                 mid = (start + end) // 2
#                 if queries[i][mid] == "?":
#                     if queries[i][end] != "?":
#                         start = mid + 1
#                     elif queries[i][start] != "?":
#                         end = mid - 1
#                     else:
#                         # start, end 전부 ? 이면 -> 길이만 같으면 된다.
#                         break
#                 else:  # mid 가 물음표가 아니면,,
#                     if queries[i][mid] == word[mid]:
#                         if queries[i][start] != "?" and queries[i][end] != "?": # 둘다 물음표 아닌 경우
#                             if queries[i][start] == word[start] and queries[i][end] == word[end]:
#                                 start += 1
#                                 end -= 1
#                             else:
#                                 state = False
#                                 break
#                         elif queries[i][start] != "?":
#                             end = end - 1
#                         elif queries[i][end] != "?":
#                             start = start + 1
#                         else: # 둘 다 물음표인 경우
#                             break
#                     else:
#                         state = False
#                         break
#
#             if state:
#                 print(queries[i], end=", ")
#                 answer[i] += 1
#
#     print()
#
# print(answer)
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for i in queries:
        if i[0] != "?":
            ans = count_by_range(array[len(i)], i.replace('?', 'a'), i.replace('?', 'z'))
        else:
            ans = count_by_range(reverse_array[len(i)], i[::-1].replace('?', 'a'), i[::-1].replace('?', 'z'))
        answer.append(ans)
    return answer
