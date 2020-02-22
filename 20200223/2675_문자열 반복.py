T = int(input())
S = dict()

for _ in range(T):
    repeat, words = input().split()
    output = ''
    for word in words:
        output += word * int(repeat)
    print(output)