### Basic Code ### 

# 10진수 = Decimal
# 2진수 = Binary
# 8진수 = Octal
# 16진수 = Hexa Decimal

# 10진수 -> 2,8,16진수 변환
print("10진수 -> 2진수: ",bin(42))
print("10진수 -> 8진수: ",oct(42))
print("10진수 -> 16진수: ",hex(42),"\n")

# 2,8,16진수 -> 10진수 변환
print("2진수 -> 10진수: ",int('0b101010',2))
print("8진수 -> 10진수: ",int('0o52',8))
print("16진수 -> 10진수: ",int('0x2a',16))