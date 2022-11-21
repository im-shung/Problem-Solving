# 참고 - https://codingdog.tistory.com/entry/%EA%B0%80%ED%9D%AC%EC%99%80-%ED%82%A4%EC%9B%8C%EB%93%9C-equal-%EC%97%B0%EC%82%B0%EC%9D%B4-%EB%93%A4%EC%96%B4%EC%98%A4%EB%A9%B4-hashmap%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EB%A9%B4-%EC%A2%8B%EB%8B%A4

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs = sys.stdin.read().split()
    keywords = set(inputs[:N])
    blogs = inputs[N:]
    for blog in blogs:
        words = set(blog.split(","))
        keywords -= words
        print(len(keywords))
