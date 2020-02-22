num = int(input())
hansu = 0

for n in range(1, num + 1):
    if n < 100:
        hansu += 1

    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1
    
print(hansu)

"""
두자리수까지는 모두 한수라고 가정하고 3자리수일 경우에만 사용할 수 있는 알고리즘을 만들면 되었지만, 이상한 알고리즘을 만들게 되어서 결국 풀이를 보게 되었다.
풀이 링크 : https://roseline124.github.io/algorithm/2019/03/29/Algorithem-baekjoon-1065.html
"""