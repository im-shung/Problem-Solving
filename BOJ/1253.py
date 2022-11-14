import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))

    # 배열 정렬
    s.sort()

    # ans: 다른 두 수의 합으로 나타낼 수 있는 수의 개수
    ans = 0

    # 각 수(s[i])에 대한 반복문
    for i in range(n):
        target = s[i]

        left = 0
        if left == i: # 예외처리 - 합으로 나타내려는 수와 겹치는 index
            left += 1

        right = n - 1
        if right == i:
            right -= 1

        # 투 포인터 구현
        while left < right:
            current_sum = s[left] + s[right]
            if current_sum == target:
                ans += 1
                break
            elif current_sum > target:
                right -= 1
                if right == i: # 예외처리 - 합으로 나타내려는 수와 겹치는 index
                    right -= 1
            else:
                left += 1
                if left == i:
                    left += 1

    print(ans)