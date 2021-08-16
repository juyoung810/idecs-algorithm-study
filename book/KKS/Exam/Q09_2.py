def solution(s):
    answer = int(1e9)
    if len(s) == 1:
        return 1

    for delta in range(1, len(s)//2 + 1):
        result = ''
        cnt = 1
        unit = s[:delta]

        for i in range(delta, len(s) + delta, delta):
            if unit == s[i:i+delta]:
                cnt += 1
            else:
                if cnt == 1:
                    result += unit
                else:
                    result += str(cnt) + unit
                unit = s[i:i+delta]
                cnt = 1
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc"))