import sys


def get_pisano(m):

    p = 0
    c = 1

    for i in range(m*m):
        p, c = c, (p + c) % m

        if p == 0 and c == 1:
            return i + 1


def get_fib(n, m):

    pisano_per = get_pisano(m)

    n = n % pisano_per

    p, c = 0, 1

    if n==0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        p, c = c, p + c


    return(c % m)



def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n, m = map(int, sys_in.readline().split())

    print(get_fib(n, m))

if __name__ == '__main__':
    main()