import sys
input =  sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
D = list(map(int, input().split()))

maxi = -1e09
mini = 1e09

def cal(idx, number):
    global maxi, mini
    if idx == n:
        maxi = max(maxi, number)
        mini = min(mini, number)
        return 
    
    if D[0]:
        D[0] -= 1
        cal(idx + 1, number + A[idx])
        D[0] += 1
    if D[1]:
        D[1] -= 1
        cal(idx + 1, number - A[idx])
        D[1] += 1
    if D[2]:
        D[2] -= 1
        cal(idx + 1, number * A[idx])
        D[2] += 1
    if D[3]:
        D[3] -= 1
        if number < 0:
            number = number * -1 // A[idx] * -1
        else:
            number = number // A[idx]
        cal(idx + 1, number)
        D[3] += 1

cal(1, A[0])


print(int(maxi))
print(int(mini))