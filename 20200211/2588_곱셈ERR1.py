#RUNTIME ERROR
A, B = map(int, input().split())
print(A * (B % 10))
print(A * (B % 100 // 10))
print(A * (B // 100))
print(A * B)