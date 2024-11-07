from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

answer = []

word_dict = defaultdict(lambda : [0, 0, ""])
for i in range(n):
    word = input().strip()
    if len(word) >= m:
        word_dict[word][0] -= 1
        word_dict[word][1] = -len(word)
        word_dict[word][2] = word

for value in word_dict.values():
    answer.append(value)

answer.sort()

for word in answer:
    print(word[2])



