import sys
import random


def partition(A, l, r):
    lt = l
    i = l
    gt = r
    pivot = A[l]

    while i<=gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt+=1
            i+=1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt-=1
        else:
            i+=1

    return lt, gt


def quick_sort(A, l, r):
    
    if l >= r:
        return
    
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]

    m1, m2 = partition(A, l, r)

    quick_sort(A, l, m1-1)
    quick_sort(A, m2+1, r)


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    arr = list(map(int, sys_in.readline().split()))

    quick_sort(arr, 0, n-1)

    print(*arr, sep = ' ')
    

if __name__ == '__main__':
    main()
