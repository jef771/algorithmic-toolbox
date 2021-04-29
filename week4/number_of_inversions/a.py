import sys


def merge_sort(arr, i_low):
    if len(arr) > 1:
        mid = len(arr)//2
        low = arr[:mid]
        high = arr[mid:]

        merge_sort(low, i_low)
        merge_sort(high, i_low)

        i, j, k = 0, 0, 0

        while i<len(low) and j<len(high):
            if low[i] < high[j]:
                arr[k] = low[i]
                i+=1
    
            else:
                arr[k] = high[j]
                i_low+=1
                j+=1
                
            k+=1

        while i < len(low):
            arr[k] = low[i]
            i+=1
            k+=1
            

        while j < len(high):
            arr[k] = high[j]
            j+=1
            k+=1
            

        return i_low


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())
    arr = list(map(int, sys_in.readline().split()))

    print(merge_sort(arr, 0))




if __name__ == '__main__':
    main()