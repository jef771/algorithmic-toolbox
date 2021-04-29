import sys


def longest(arr1, arr2):
    n,m = len(arr1), len(arr2)
    lcs = [[0]*(m+1) for x in range(n+1)]

    for i in range(n):
        for j in range(m):
            if arr1[i] == arr2[j]:
                lcs[i+1][j+1] = lcs[i][j]+1
            else:
                lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j]) 

    return max(max(lcs))


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n1 = int(sys_in.readline())
    arr1 = list(map(int, sys_in.readline().split()))

    n2 = int(sys_in.readline())
    arr2 = list(map(int, sys_in.readline().split()))

    
    print(longest(arr1, arr2))



if __name__ == '__main__':
    main()