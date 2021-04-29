import sys


def get_gcd(a, b):

    R = 0

    while (a%b) > 0:
        R = a%b
        a = b
        b = R

    return b


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    a, b = map(int, sys_in.readline().split())

    print(get_gcd(a, b))


if __name__ == '__main__':
    main()