numbers = list(map(int, input().split()))

u = sum(numbers)

min_n = u - max(numbers)
max_n = u - min(numbers)

print(min_n, max_n)