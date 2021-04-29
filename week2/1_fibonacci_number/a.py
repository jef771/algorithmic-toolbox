import sys


def get_fib(n):

    fib_list = [0, 1]

    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    
    return fib_list[n]

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    print(get_fib(n))


if __name__ == '__main__':
    main()