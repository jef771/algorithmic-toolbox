import sys


def binary_search(a, n, target):
    L, R = 0, n-1

    while L<=R:
        mid = L + (R-L) // 2

        if a[mid] == target:
            return mid
        elif a[mid] < target:
            L = mid + 1
        else:
            R = mid - 1

    return -1


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    arr1 = list(map(int, sys_in.readline().split()))
    arr2 = list(map(int, sys_in.readline().split()))
    n1, n2 = arr1[0], arr2[0]
    arr1 = arr1[1:]
    arr2 = arr2[1:]

    for i in arr2:
        sys_out.write(f'{binary_search(arr1, n1, i)} ')



if __name__ == '__main__':
    main()