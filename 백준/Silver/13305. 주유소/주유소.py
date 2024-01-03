import sys
input = sys.stdin.readline
n = int(input())
dis=list(map(int, input().split()))
cost=list(map(int, input().split()))
result = 0

for i in range(n-1):
    if cost[i]>cost[i+1]:
        result += cost[i]*dis[i]
    else:
        result += cost[i]*dis[i-1]
print(result)