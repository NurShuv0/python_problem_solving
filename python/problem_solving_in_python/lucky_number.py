# a = int(input())
# b = int(input())
a, b = map(int, input().split())
ok = False
for i in range(a, b+1):
    flag = False
    temp = i
    # print(i)
    while(temp > 0):
        rem = temp % 10
        # print(rem)
        temp //= 10
        # print(temp)
        if rem != 4 and rem != 7:
            flag = True
            break
    if not flag:
        ok = True
        print(i, end = " ")
if not ok : 
    print(-1)