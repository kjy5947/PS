n = int(input())
arr = list(map(int, input().split()))

seq = [0 for _ in range(n)]
#seq = [0]*n

for i in range(n):
    for j in range(n):
        if arr[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            arr[i] -= 1

for a in seq:
    print(a, end=' ')

