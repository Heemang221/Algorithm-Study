import sys

data = [int(sys.stdin.readline()) for _ in range(9)]
max(data)
print(max(data))
print(data.index(max(data))+1)
