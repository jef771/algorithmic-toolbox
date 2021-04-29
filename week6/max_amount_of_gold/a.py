import sys


def max_gold_amount(W, gold_list):
    n, m = len(gold_list), W

    lcs = [[0]*(n+1) for x in range(m+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            lcs[w][i] = lcs[w][i-1]
            if gold_list[i-1]<=w:
                val = lcs[w-gold_list[i-1]][i-1] + gold_list[i-1]
                lcs[w][i] = max(lcs[w][i], val)


    return lcs[m][n]



def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    W, n = map(int, sys_in.readline().split())

    gold_list = list(map(int, sys_in.readline().split()))

    gold_list.sort()

    print(max_gold_amount(W, gold_list))


if __name__ == '__main__':
    main()