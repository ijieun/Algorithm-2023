import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    s, e = map(int, input().split())
    li.append([s, e])
li.sort(key = lambda x :(x[1], x[0]))

now = 0
count = 0
for i in li:
    if i[0]>=now:
        count += 1
        now = i[1]
        
print(count)