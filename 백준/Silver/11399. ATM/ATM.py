import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
sum = 0
result=0
li.sort()
for i in li:
    sum+=i
    result += sum
print(result)