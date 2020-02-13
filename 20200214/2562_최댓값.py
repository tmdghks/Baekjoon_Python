tmp = 0
for i in range(9):
    A = int(input())
    if (A > tmp):
        tmp = A
        count = i + 1
print(tmp)
print(count)