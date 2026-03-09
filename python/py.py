import math
import sys

def solve(): 
    n, m, d = map(int, sys.stdin.readline().split())
    x = d // m
    x += 1
    ans = math.ceil(n/x)
    print(ans)


def main(): 
    input = sys.stdin.readline
    t = int(input())
    for i in range(t):
        solve()


if __name__ == "__main__":
    main()