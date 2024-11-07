"""문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수, C는 109보다 작거나 같은 음이 아닌 정수이다. 둘째 줄에 물건의 무게가 주어진다. 무게도 109보다 작거나 같은 자연수이다.

출력
첫째 줄에 가방에 넣는 방법의 수를 출력한다."""

import sys
from itertools import combinations
input = sys.stdin.readline

n, c = list(map(int, input().split()))
weights = list(map(int, input().split()))

a = weights[: n // 2]
b = weights[n // 2 :]

list_a = [0]
list_b = [0]

for i in range(1, len(a) + 1):
    for combi_list in combinations(a, i):
        list_a.append(sum(combi_list))

for i in range(1, len(b) + 1):
    for combi_list in combinations(b, i):
        list_b.append(sum(combi_list))
list_a.sort()
list_b.sort()
    
i = 0
j = len(list_b) - 1

answer = 0
while i < len(list_a) and j >= 0:
    if list_a[i] + list_b[j] <= c:
        answer += j + 1
        i += 1
    else:
        j -= 1
print(answer)