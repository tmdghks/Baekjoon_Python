S = list(map(str, input()))
location = [-1] * 26
for i in range(len(S)):
    if location[ord(S[i]) - 97] == -1:
        location[ord(S[i]) - 97] = i
for i in location:
    print(i)
"""
오늘 알게 된 점
list는 * 연산자로 반복이 가능하다.
"""