from collections import Counter

arr = [1, 10, 4 ,13, 8, 3, 1, 7]

counter = Counter(arr);
print(counter)

# 최소값 구하기 
min = min(arr)
print(min)

# 최소값 개수 구하기
index = counter[min]
print(index)

# 최소값 개수가 여러 개일 때 최소값 인덱스 구하기
result = list(filter(lambda x: arr[x] == min, range(len(arr))))
print(result)

# 튜플 리스트 정렬하기
# sorted(arr, key = lambda x: (x[0], x[1]))