import sys
input = sys.stdin.readline
  
n = int(input(),8) # 8진수를 10진수로 변환
print(bin(n)[2:]) # 10진수를 2진수로 변환 + '0b'제거해서 출력 