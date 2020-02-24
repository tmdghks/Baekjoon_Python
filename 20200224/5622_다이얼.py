sec_list = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
word = input()
time = 0
for w in word:
    time += sec_list[ord(w) - 65]
print(time)