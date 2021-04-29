import sys


def get_sum(deque1, deque2):

    ans, temp = 0, 0

    while deque1:
        temp = deque1[-1] * deque2[-1]
        ans+=temp
        deque1.pop()
        deque2.pop()

    return ans


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    list1 = list(map(int, sys_in.readline().split()))
    list2 = list(map(int, sys_in.readline().split()))

    list1.sort()

    list2.sort()
    

    sys_out.write(f'{get_sum(list1, list2)}\n')


if __name__ == '__main__':
    main()