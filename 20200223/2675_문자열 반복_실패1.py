T = int(input())
for i in range(T):
    tmp = input().split()
    new_P = []
    R = int(tmp[0])
    P = list(map(str, tmp[1]))
    for i in range(len(P)):
        new_P += P[i] * R
for i in new_P:
    print(i)