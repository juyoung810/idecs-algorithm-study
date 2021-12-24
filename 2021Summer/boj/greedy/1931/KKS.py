#입력세팅
cnt = 0
n = int(input())
meeting_info = []
for i in range(n):
    _temp = list(map(int, input().split()))
    meeting_info.append(_temp)
#다익스트라 알고리즘 -> 단순하게 생각해보자
#일단 가장 빨리 시작하는 회의를 찾고
#끝나는 시간 이후로 시작하는 회의를 찾기를 반복 ->더이상 회의 없으면 종료하고 횟수 출력

# #가장 빠른 시간 찾기
def find_meeting(meeting_info):
    global cnt
    fastest_time = float("inf")
    fastest_meeting = None
    for meeting in meeting_info:
        if meeting[0] < fastest_time:
            fastest_time = meeting[0]
            fastest_meeting = meeting
    meeting_info.remove(meeting)
    cnt += 1
    return fastest_meeting
#리스트 업데이트
def update_meeting_info(end_time, meeting_info):
    for meeting in meeting_info:
        if meeting[0] < end_time:
            meeting_info.remove(meeting)

while True:
    if len(meeting_info) == 0:
        break
    fastest_meeting = find_meeting(meeting_info)
    update_meeting_info(fastest_meeting[1], meeting_info)

print(cnt)






