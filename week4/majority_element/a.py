import sys


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    arr = list(map(int, sys_in.readline().split()))
    

    counts={}
    for i in range(len(arr)):
        counts[arr[i]] = counts.get(arr[i], 0)+1
        if counts[arr[i]] > n//2:
            print(1)
            sys.exit()

    print(0)


if __name__ == '__main__':
    main()