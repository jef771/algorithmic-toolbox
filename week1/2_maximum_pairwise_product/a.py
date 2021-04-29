import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    arr = list(map(int, sys_in.readline().split()))
    arr.sort();
    
    print(arr[n-1] * arr[n-2])

if __name__ == '__main__':
    main()