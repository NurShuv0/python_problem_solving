n = int(input())

if n <= 1:
    for _ in range(n):
        print(int(input()))
else:
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)

    mx = max(arr)
    mn = min(arr)

    mx_idx = arr.index(mx)
    mn_idx = arr.index(mn)

    arr[mx_idx], arr[mn_idx] = arr[mn_idx], arr[mx_idx]

    for i in arr:
        print(i)