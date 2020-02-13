#세 수의 곱 구하기
A = 1
for i in range(3):
    A = A * int(input())
#정수 A를 문자열 A로 변환하기
A = str(A)
#문자 i의 개수를 출력함
#이 for문은 i의 값이 0에서 9일 때까지 작동함
for i in range(10):
    print(A.count(str(i)))