arr = input()

stk = list()
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stk.append(arr[i])
    else:# )
        if arr[i-1] == '(':
            stk.pop()
            cnt += len(stk)
        else:
            stk.pop()
            cnt += 1
print(cnt)
