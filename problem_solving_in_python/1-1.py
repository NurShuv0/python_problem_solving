t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    nur = list(input())
    for i in range(1,n - 1):
        if nur[i-1] == '1' and nur[i+1] == '1':
            nur[i] = '1'
            i += 1
    mx = nur.count('1')
    # print(str)
    # print(mx) 
    for i in range(1, n-1):
        if nur[i-1] == '1' and nur[i+1] == '1':
            nur[i] = '0'
            i += 1
    mn = nur.count('1')
    print(mn, mx)

