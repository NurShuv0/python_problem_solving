t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    div = []
    for i in range(1, int(n **.5) + 1):
        if n % i == 0:
            div.append(i)
            if i == n//i:
                break
            else :
                div.append(n//i)
    pref_s = []
    pref_s.append(arr[0])
    for i in range(1,n):
        pref_s.append(pref_s[i-1] + arr[i])
    ans = 0
    for i in div:
        mx = float('-inf')
        mn = float('inf')
        left = 0
        for j in range(0,n,i):
            mx = max(mx, pref_s[j + i -1] - left)
            mn = min(mn, pref_s[j + i - 1] - left)
            left = pref_s[i + j - 1]
        ans = max(ans, mx - mn)
    print(ans)
