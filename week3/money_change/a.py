import sys

def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    ans = 0
    while n:
        while n>=10:
            n-=10
            ans+=1
        while n>=5:
            n-=5
            ans+=1
        while n>=1:
            n-=1
            ans+=1

    print(ans)


if __name__ == '__main__':
    main()