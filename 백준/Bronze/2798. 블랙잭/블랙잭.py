import sys
input = sys.stdin.readline
n , m = map(int, input().split())
li = list(map(int, input().split()))
result=0
for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            if i != j and j != k and i != k:
                if li[i]+li[j]+li[k] <= m:
                    if li[i]+li[j]+li[k]>=result:
                        result = li[i]+li[j]+li[k]
print(result)