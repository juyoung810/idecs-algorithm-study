def solution(s):
    if len(s) == 1:
        return 1
    len_result = []
    result = ""
    for cut in range(1, len(s) // 2 + 1):
        # 처음부터 잘라야하기 떄문에 cnt 1로 놓음(자기 자신)
        cnt = 1
        unit = s[:cut]
        # 자기 뒤에있는 문자열들 cut을 step size로 가져가면서 순회
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == unit:
                # 같으면 cnt에 1더해줌
                cnt += 1
            else:  # 만약에 다르면
                if cnt == 1:  # 다르고 cnt가 1이면(바로 맞지않는경우 당하는경우)
                    cnt = ""
                result += str(cnt) + unit  # 일단 결과 cnt(1이면 생략) + unit 넣고
                unit = s[i:i + cut]  # unit을 업데이트시켜줌
                cnt = 1
        # 마지막에 왔을때
        if cnt == 1:
            cnt = ""
        result += str(cnt) + unit
        len_result.append(len(result))
        result = ""

    return min(len_result)