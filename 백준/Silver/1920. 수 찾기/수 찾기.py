import sys
input = sys.stdin.readline
_ = int(input())
N=map(int, input().split())
_ = int(input())
M=map(int, input().split())
hashmap = {}

for n in N:
    if n in hashmap:
        hashmap[n]+=1
    else:
        hashmap[n]=1
for m in M:
    if m in hashmap:
        print(1)
    else:
        print(0)