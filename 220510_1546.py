n = int(input())
score = list(map(int, input().split()))
max = max(score)
new = []

for i in range(n):
    new.append(score[i]/max*100)

print(sum(new)/n)
