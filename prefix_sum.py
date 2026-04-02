n, q = map(int, input().split())
arr = list(map(int, input().split()))

pref_sum = [0] * (n)
pref_sum[0] = arr[0]
for i in range(1, n):
    pref_sum[i] = (pref_sum[i-1] + arr[i])
# print(pref_sum)

for i in range(q):
    left , right = map(int, input().split())
    if left == 1:
        result = pref_sum[right-1]
    else : 
        result = (pref_sum[right - 1] - pref_sum[left - 2])
    print(result)
