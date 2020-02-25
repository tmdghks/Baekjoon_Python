a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
print(len(alpha))

# 알게된 점
# replace함수를 통해 문자열의 내용을 바꿀 수 있다는 것을 알게 되었다.