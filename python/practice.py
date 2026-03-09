import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        
        ans = 0
        for i in range(1, n):
            if v[i] == v[i - 1] or v[i] == 7 - v[i - 1]:
                ans += 1
                v[i] = 0
        
        print(ans)

if __name__ == "__main__":
    solve()