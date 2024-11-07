import sys
input = sys.stdin.readline

numbers = [i for i in range(1000001)]
for i in range(2, 1001):
    numbers[i ** 2] -= i

n = int(input())
if n < 2:
    print(n)
else:
    for i in range(2, n + 1):
        tmp = 1
        for j in range(2, int(n ** (1 / 2) + 1)):
            if i % j == 0:
                tmp += j + i // j

        numbers[i] = numbers[i - 1] + i + tmp
    print(numbers[n])