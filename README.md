# idecs-algorihm-study

---

>아이덱스 2021 하계 여름 방학 알고리즘 스터디를 위한 저장소입니다.

## Programming Language

---

+ python
+ 기본으로 python 언어를 사용하여 코드를 작성, 해설한다.
+ 추가적으로 다른 언어를 사용하여 푼 경우 해당 코드를 올리는 것은 자유

## 알고리즘 사이트

---
+ baekjoon: https://www.acmicpc.net/

## 폴더 구조

---
+ 사이트 폴더 - 문제 폴더 - 소스코드 및 풀이 방법 파일
    + 예) boj -> 1000 -> juyoung.py, 풀이방법.md
+ 소스코드: 자신의 이름, 별명, 아이디 중 하나 .확장자명 으로 작성한다.
    + 예) juyoung.py, juyoung.cpp, juyoung.java
  
+ 풀이방법: 자신의 이름 혹은 아이디 뒤에 _풀이방법.md 로 작성한다.
  + 예) juyoung_풀이방법.md
  

## 스터디 Rule

---
+  "이것이 취업을 위한 코딩 테스트다. with Python" 이틀에 1 part 씩 공부
+  해당 part의 예제 풀이 후 소스 코드 PR 필수
+  선정된 4문제 중 하나 반드시 풀이 후 해설 준비
+  문제 풀이 후 해당 문제 폴더에 자신의 소스코드 PR
+  다 풀지 못하더라도 pseudo code 또는 아이디어 제시 후 PR 해보기!
+  두 시간이상 고민했더라도 풀지 못할 경우, 잘 정리된 코드 찾아본 후 분석 , 정리 후 PR 권장
+  해설 내용: 문제 접근 방법, 시간 복잡도 , 공간 복잡도 등등,, 내용 설명
+  해설 내용은 @juyoung810 이 정리 후 풀이 방법.md 파일로 올릴 예정(참고)
+  추가로 추천하고 싶은 문제가 있을 경우 폴더 rule 에 맞게 폴더 생성 후 알려주기

## Git 사용 방법

---
#### 1. git 설치  
https://git-scm.com/downloads (자세한건 검색하기)
#### 2. git clone
1. https://github.com/juyoung810/idecs-algorithm-study repository 에 오른쪽 상단 fork 버튼 클릭
2. #####자신의 repository로 이동 후 fork 한 자신의 repository의 초록색 code 버튼 아래의 주소 복사
3. 다운로드하길 원하는 폴더의 위치로 이동 후 터미널 창에

       git clone [복사한 url]

4. 해당 폴더로 이동 후 폴더 안에서 마우스 오른쪽 클릭 후 "Git Bash Here"  클릭
5. 자신의 branch 생성하기

          git branch [자신의이름 or 별명 or 아이디 중 마음대로 하나]

6. 생성한 branch로 이동

        git checkout [생성한 branch 이름]
7. 주영의 repository 와 내가 만든 로컬 동기화 하기 위해 주소 추가

        git remote add upstream https://github.com/juyoung810/idecs-algorithm-study.git



#### 3. 주영의 repository 의 내용 받아 오고 싶을 때  (동기화) -> 주영거랑 내거랑 달라진게 없으면 안해도 됨!
> 항상 문제가 올라오니, 웬만하면 내용 받아오고 문제풀이 시작하는게 좋음!

1. 주영의 repsitory(upstream으로 저장해 놓음)의 내용을 받는다.
   
            git fetch upstream
   
2.  자신이 만든 branch가 아닌 main으로 이동
    
            git checkout main
    
3.  나의 main과 주영의 repository(upstream) 합치기

        git merge upstream/main

4.  나의 branch로 이동

        git checkout <내가 만든 브런치>

5.  주영의 내용과 합친 나의 main을 나의 branch와 합치기   

        git merge main

#### 4. 각각 해당하는 폴더에 자신의 소스 코드 작성
   + 소스 코드 작성이전에 자신이 생성한 브런치인지 확인 -> 이미 자기 branch면 안해도 됨
   
          git checkout [자신이 생성한 브런치]
   -> 소스 코드 작성하기

#### 5. 내가 작성한 소스 코드 올리기 (주영거에 올리는 거)
1. staging 영역에 추가

          git add .

2. repository에 commit

          git commit -m "커밋 메세지 자유"

    + 처음 commit 할 시 *** Please tell me who you are. 메세지가 뜬다. 
    
            git config --global user.email [you@example.com]

        !! git 에 한번도 commit 해본 적 없는 경우 하면 됨.

3. 원격 저장소의 main branch 에 푸쉬
  
          git push origin [자신의 브런치 이름]

4. PR 날리는 법 ()
    1. 자신의 원격 git repository 로 이동 : https://github.com/[본인 아이디]/idecs-algorithm-study
    2. issue 옆 pull request 버튼 클릭 
       + base repository : juyoung810/.. base:main <- head repository: 자기 아이디/.. compare: 자신이 만든 branch 
    3. create pull request 버튼 계속 클릭!! -> 모르겠으면 pull request 날리는 법 검색 해보기!
    


          



     






  
    
    




