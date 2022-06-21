### Basic Code ### 

# 문자열을 한 글자씩 배열에 저장

# 입력값
# 3
# AAAA 
# ABCA 
# AAAA

# 결과값
# arr = [['A', 'A', 'A', 'A'],
#        ['A', 'B', 'C', 'A'],
#        ['A', 'A', 'A', 'A']]

arr = [list(input()) for _ in range(int(input()))]
print(arr)