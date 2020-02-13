#source : https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-1110%EB%B2%88-%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4
tmp = inp = int(input())
count = 0
while True:
    ten = tmp // 10
    one = tmp % 10
    res = ten + one
    count = count + 1
    tmp = int(str(tmp%10)+str(res%10))
    if (tmp == inp):
        break
print(count)