import sys
input = sys.stdin.readline
s = int(input().rstrip())
for i in range(1,s+1):
    if s<i:
        print(i-1)
        break
    if s==1:
        print(1)
    s-=i