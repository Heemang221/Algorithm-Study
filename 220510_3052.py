numbers = []
na = []

for _ in range(10):
    numbers.append(int(input()))

for i in range(10):
    na.append(numbers[i] % 42)

print(len(set(na)))
