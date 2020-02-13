import sys
T = int(input())
for s in sys.stdin:
    print(sum(map(int, s.split())))