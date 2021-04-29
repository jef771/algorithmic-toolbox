import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    a, b = map(int, sys_in.readline().split())

    print(a+b)


if __name__ == '__main__':
    main()