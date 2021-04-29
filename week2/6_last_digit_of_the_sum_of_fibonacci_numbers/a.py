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

    p, c, ans = 0, 1, 0


    if n==0:
        return 0
    elif n == 1:
        return 1
    for i in range(n):
        ans += c
        p, c = c, p + c

    return(ans%10)



def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n= int(sys_in.readline())

    print(get_fib(n, 1000))

if __name__ == '__main__':
    main()