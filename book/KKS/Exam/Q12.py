def solution(n, build_frame):
    #구현해야할 기능
    answer = [[]]
    # build_frame을 돌면서 작업 체크 -> 조건확인해서 맞으면 -> result에 추가
    # 중간에 삭제되면 이전에는 건설 가능했던게 불가능 해질수도 -> 다시한번 체크
    map = [[0] * (n+1) for _ in range(n+1)]
    for task in build_frame:
        x, y, build_type, task_type = task
        if build_type == 0: #기둥에 관한 작업이면
            if task_type == 1: #설치 작업이면
                check_task(x, y, build_type, map, answer)
            else: # 삭제 작업이면
                pass
        else: #보에 관한 작업이면
            if task_type == 1: #설치 작업이면
                check_task(x, y, build_type, map, answer)
            else: # 삭제 작업이면
                pass

    return answer

def check_task(x,y, build_type, map, answer):
    if build_type == 0: #기둥이면
        if y < 1: #바닥에 설치하는 경우
            map[x][y] == 1
            answer.append([x,y,build_type])
        else: #바닥이 아닌경우
            if map[x][y-1] == 1:
                map[x][y] == 1
                answer.append([x, y, build_type])
    else: #보
        if map[x-1][y] == 1:
            map[x][y] == 1
            answer.append([x, y, build_type])

def verify_delete(x,y, build_type, map, answer):
    if build_type == 0: #기둥삭제
        # 내 위에 다른 기둥이 있을때
        if map[x][y+1] == 1:
            return
        if (map[x+1][y] == 1) 1 or
    else: #보 삭제
        #내 양 옆이 보인경우
        #보 위에 기둥이 있는경우
        #내가 없어짐으로써 연결이 끊기는 보가 존재하는 경우