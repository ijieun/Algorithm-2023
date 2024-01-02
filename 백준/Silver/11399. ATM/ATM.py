import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
sum = 0
result=0
sorted_li = sorted(li)
for i in sorted_li:
    sum+=i
    result += sum
print(result)