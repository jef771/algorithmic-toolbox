import sys


def sub_array_sum(nums, W):
    
    ans = 0
    n = len(nums)

    lcs = [[0]*(n+1) for x in range(W+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            lcs[w][i] = lcs[w][i-1]
            if nums[i-1]<=w:
                val = lcs[w-nums[i-1]][i-1] + nums[i-1]
                lcs[w][i] = max(lcs[w][i], val)
            if lcs[w][i] == W:
                ans+=1
    
    return ans >= 3


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    nums = list(map(int, sys_in.readline().split()))

    W = sum(nums)

    if n<3 or W%3!=0:
        sys_out.write('0')
    else:
        print(int(sub_array_sum(nums, W//3)))



if __name__ == '__main__':
    main()