import sys


def get_best(p, wt):
    value_dict = {}

    for i in range(len(p)):
        temp = p[i]/wt[i]
        value_dict[temp] = i 

    return value_dict


def knapsack(W, n, p, wt, values):
    ans = 0

    while W:
        
        if len(values) >= 1:
            i = values[(max(values))]
            v = p[i]/wt[i]
            
        while wt[i] > 0 and W > 0:
    
            wt[i] = wt[i] - 1
            W-=1
            ans+=v

        
        del values[(max(values))]
        

    return ans


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n, W = map(int, sys_in.readline().split())

    p = [0] * n
    wt = [0] * n

    for i in range(n):
        p[i], wt[i] = map(int, sys_in.readline().split())

    if sum(wt) < W:
        print(f'{sum(p):.4f}')
        sys.exit()
        
    value_dict = get_best(p, wt)

    
    print(f'{knapsack(W, n, p, wt, value_dict):.4f}')

if __name__ == '__main__':
    main()