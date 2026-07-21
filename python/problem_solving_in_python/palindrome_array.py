n = int(input())
arr = list(map(int,input().split()))
# print(arr)
rev = arr.copy()
rev.reverse()
# print(rev)
if rev == arr: 
    print("YES")
else :
    print("NO")