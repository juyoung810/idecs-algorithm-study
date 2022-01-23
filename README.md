# idecs-algorithm-study

> 아이덱스 파이썬 알고리즘 스터디

## Programming Language
+ python를 사용하여 코드를 작성, 해설한다.
+ 추가적으로 다른 언어를 사용하여 푼 경우 해당 코드를 올리는 것은 자유
+ pycharm 툴 사용 추천

## 알고리즘 사이트

+ baekjoon: https://www.acmicpc.net/

---

## 폴더 구조

+ 자신의 이름 - 사이트 폴더 - 문제 폴더 - 소스코드 및 풀이 방법 파일
    + 예) juyoung -> boj -> 1000 -> juyoung.py, 풀이방법.md
  
+ 풀이방법:
    +  각 part 별 자신이 해설해야 하는 문제는 `.md` 파일로 반드시 풀이 작성
    +  풀이하는 문제가 아닌, 개인 해설의 경우 자유
  
    
---
## 스터디 Rule

+ 하루에 한 문제 선정된 문제 풀이 소스 코드 PR 필수
+ 회의 전 결정된 자신의 해설 문제의 경우 풀이 `.md` 파일 작성 후 PR 필수
+ 월요일 8시 회의 시간 이전까지 PR 하지 않을 시 한 문제 당 벌금 1000원
+ 추가로 추천하고 싶은 문제가 있을 경우 폴더 rule 에 맞게 폴더 생성 후 알려주기 (recommend 폴더에)
+ 분기 별 폴더 년도/winter(summer) 폴더로 합쳐질 예정..!


---
## github 사용 방법
> 저도 잘은 모르지만,, 대충 올립니다.. 모를 경우 검색추천합니다.

### 1. github에 있는 폴더 내 로컬로 받아오는 법 (git clone 하는 법)

- 오른쪽 상단의 초록색 `code` 버튼 클릭 -> github 저장소 주소 나온다
- https 형식의 주소를 복사하기
- 터미널(cmd) 를 통해 자신의 로컬에서 폴더의 복사를 원하는 위치로 이동
- clone 명령어 입력
 `git clone https://github.com/juyoung810/idecs-algorithm-study.git`

- `git remote -v` 명령어 입력해서 원격 저장소와 연결되었는지 확인해보기

### 2. 작성한 소스코드 원격 저장소에 올리는 법 (git add, commit, push)
- 소스코드 자유롭게 자신의 폴더에 작성
- `git status` 통해 자신이 수정,추가한 파일 확인 가능
- `git add .` -> `git commit -m "(날짜) 사람이름 몇번 문제 풀이" ` -> `git push origin main`
- 위의 과정을 통해 원격 저장소에 올라가짐!
- `git commit -am "커밋 메세지 내용"` 으로 `add`, `commit` 한번에 하는 것도 가능

### 3. 원격 저장소의 변경 내용 내 로컬로 받는 방법 (git pull)
- `git pull origin main` 통해 받기 가능
- 한번 하고 나면 `git pull`로도 간단하게 가능

### (추천)❕ branch 생성 후 push
- `git branch [자신이 원하는 브랜치 명]` 통해 자신의 branch 생성
- `git checkout [자신의 branch]`
- __소스코드 작성 전 자신의 branch 현재 어디인지 확인 (main인지,,자기 branch 인지)
- `git commit -am "..."` -> `git push origin [branch]`

--> 다른 사람과 branch 같이 안쓰게 되서 remote main의 변경 사항 pull 하지않아도 
자신의 branch 의 상태 관리 가능 (pull 하지 않고 바로 작성 -> push 가능)

---
### 추가 참고 사항
- 빈 폴더는 원격 저장소에 반영 안되니 어떤 파일,,(readme.md) 파일 생성 후 올리면 반영됨
- 따로 branch 는 사용하지 않을 것 같지만 필요 시 사용법 정리하갰습니당
- 다른 사람 폴더로 잘못 올려서 큰일이 일어나지 않도록 주의,,
- md 파일 작성하는 방법을 잘 모를 시 -> 마크다운 작성방법! 으로 간단하게 알아볼 수 있음
- 여름에 작성했던 md 파일 형식을 한번 살펴보고 풀이 작성을 추천합니당
