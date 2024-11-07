import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        answer = '1'
        while True:
            if int(answer) >= n and int(answer) % n == 0:
                print(len(answer))
                break
            answer += '1'
    except:
        break