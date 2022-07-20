# SW Expert Academy 
# 4869. [파이썬 S/W 문제해결 기본 - Stack1] 4일차 - 종이붙이기 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&

T = int(input())

def gluring_paper(N):
    global sum
    if N == 1:
        return 1 
    elif N == 2:
        return 3
    elif N > 2:
        # gluring_paper(N-1) == 전체(N) - 10 x 20 부분(1: 세로 직사각형 1개)
        # gluring_paper(N-2) == 전체(N) - 20 x 20 부분(2: [1],[2],[3])
        
        # 20 x 20 부분은 다음 3가지로 붙여놓을 수 있다. 
        # [1] 20 x 20 정사각형
        # [2] 20 x 10 가로 직사각형 2개
        # [3] 10 x 20 세로 직사각형 2개
        # 그러면 3 * gluring_paper(N-2)이 맞지 않나? 싶지만
        # gluring_paper(N-1)에 10 x 20 부분(세로 직사각형 1개)이 포함되어 있기 때문에 [1],[2]경우만 고려해서 곱하기 2를 한다.
        
        return gluring_paper(N-1) + 2 * gluring_paper(N-2) 
    else:
        return

for test_case in range(1, T+1):
    N = int(input())
    print(f"#{test_case} {gluring_paper(N//10)}")
    