import sys
input = sys.stdin.readline
s= input().strip()
a = "abcdefghijklmnopqrstuvwxyz"

for i in a:
    print(s.find(i), end=' ')