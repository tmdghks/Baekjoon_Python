A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])
print("{0}".format(A if A > B else B))

# 알게된 점
# 파이썬에서 삼항연산자의 사용법을 알게 되었다.
#line 3과 4를 A = int(A[::-1])로 바꾸어 문자열을 뒤에서 부터 앞으로 나열하는 방법도 알게 되었다. 이를 통해 변수 C D를 선언하지 않아도 된다는 점도 알게 되었다.