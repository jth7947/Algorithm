import sys
input = sys.stdin.readline


def divided(histogram, start, end):
    if start == end:
        return histogram[start]
    if end - start == 1:
        return max(max(histogram[start : end]), min(histogram[start : end]) * 2)
    mid = (start + end) // 2
    
    


while True:
    H = list(map(int, input().split()))
    if H[0] == 0:
        break

