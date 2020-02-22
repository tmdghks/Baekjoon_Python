#solve라는 이름을 가진 함수 생성, 입력값은 list자료형이다.
def solve(a: list):
    #총 합을 할당할 변수 ans 초기화
    ans = 0
    #a의 길이만큼 반복
    for i in a:
        #ans에 i(a에서의 정수)를 더한 값을 할당함
        ans += i
    #ans의 갑 리턴
    return ans

"""
이 문제를 통해 알게된 점
함수를 선언한 뒤 입력값의 자료형을 할당할 수 있다는 점을 알게 되었다.
"""