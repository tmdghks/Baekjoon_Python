word = list(input().upper())

alphabet_list = [0] * 26

for i in word:
    alphabet_list[ord(i) - 65] += 1

if alphabet_list.count(max(alphabet_list)) >= 2:
    print("?")
else:
    print(chr(alphabet_list.index(max(alphabet_list)) + 65))