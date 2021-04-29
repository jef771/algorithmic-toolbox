import sys


def get_salary(digits):

    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            ans1 = int(str(digits[i]) + str(digits[j]))
            ans2 = int(str(digits[j]) + str(digits[i]))
            ans3 = max(ans1, ans2)
            if ans3 == ans2:
                digits[i], digits[j] = digits[j], digits[i]

    return ''.join(list(map(str, digits)))


def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    n = int(sys_in.readline())

    digits = list(map(int, sys_in.readline().split()))

    sys_out.write(f'{get_salary(digits)}')


if __name__ == '__main__':
    main()