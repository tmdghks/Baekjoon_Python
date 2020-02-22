#도저히 모르겠어서 풀이를 보았다. 링크 : https://this-programmer.com/entry/%EB%B0%B1%EC%A4%804673%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84
#1부터 10000까지의 자연수 집합을 만든다.
natural_numver_set = set(range(1, 10001))
#생성자가 존재하는 숫자들의 집합을 만든다.
generated_number_set = set()

#1부터 10000까지 반복
for i in range(1, 10001):
    #d(n)을 계산하는 반복문
    for j in str(i):
        i += int(j)
    #generated_number_set에 i 라는 숫자 추가
    generated_number_set.add(i)

#자연수 전체 집합에서 생성자가 존재하는 숫자 집합을 뺀 집합을 구함
self_number_set = natural_numver_set - generated_number_set

#위의 차집합의 모든 원소를 출력함
for i in sorted(self_number_set):
    print(i)