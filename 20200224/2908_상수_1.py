A, B = map(str, input().split())
C = int(A[2] + A[1] + A[0])
D = int(B[2] + B[1] + B[0])
print("{0}".format(C if C > D else D))

# 알게된 점
# 파이썬에서 삼항연산자의 사용법을 알게 되었다.
#line 3과 4를 A = int(A[::-1])로 바꾸어 문자열을 뒤에서 부터 앞으로 나열하는 방법도 알게 되었다.