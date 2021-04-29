import sys


def calculator(n):

    dp = [-1,0]
    arr = [0,1]

    for i in range(2,n+1):
        count_3 = count_2 = count_1 = n
        if i%3 == 0:
            count_3 = dp[i//3]
        if i%2 == 0:
            count_2 = dp[i//2]
        if i-1 >=0:
            count_1 = dp[i-1]

        dp.append(min(count_3+1, count_2+1, count_1+1))
        
        if count_3<=min(count_2, count_1):
            arr.append(i//3)
        elif count_2<=min(count_3, count_1):
            arr.append(i//2)
        elif count_1 <=min(count_3, count_2):
            arr.append(i-1)

    print(dp[n])
    arr_2=[n]
    for i in range(dp[n]):
        arr_2.append(arr[n])
        n = arr[n]
    arr_2.reverse()

    return arr_2


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline().rstrip())
    
    print(*calculator(n), sep = " ")


if __name__ == '__main__':
    main()