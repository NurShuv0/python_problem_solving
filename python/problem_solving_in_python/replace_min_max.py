n = int(input())
arr = list(map(int, input().split()))
# arr = []
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# print(arr)
mx = max(arr)
mn = min(arr)
mx_idx = arr.index(mx)
mn_idx = arr.index(mn)
arr[mx_idx] = mn
arr[mn_idx] = mx
for i in arr : 
    print(i, end = " ")

# print(arr)

