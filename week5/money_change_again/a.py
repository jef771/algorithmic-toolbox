import sys

sys_in = sys.stdin
sys_out = sys.stdout

def coin_change_min(coins, n):

    dp = [0] + [float('inf')]*n

    for coin in coins:
        for i in range(coin, n+1):
            dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[n]


def main():

    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline().rstrip())

    coins = [1,3,4]

    sys_out.write(f'{coin_change_min(coins, n)}')



if __name__ == '__main__':
    main()
