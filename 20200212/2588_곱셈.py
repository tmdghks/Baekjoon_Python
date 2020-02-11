A = int(input())
B = int(input())
print("%d\n%d\n%d\n%d"%(((B % 10) * A), (((B % 100) // 10) * A), ((B // 100) * A), (A * B)))
#오류 해결 방법 : A, B = map(int, input().split())에서 A와 B를 따로따로 입력해주니 런타임 에러가 해결되었다. 이유는 잘 모르겠다.