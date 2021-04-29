import sys


def get_stops(d, m, stops, n):
    n_r, c_r, r= 0, 0, m

    while c_r <= n:
        l_r = c_r
        while c_r <= n and (stops[c_r + 1] - stops[l_r]) <= m:
            c_r+=1

        if c_r == l_r:
            return -1
        else:
            n_r+=1
            

    return n_r-1



def main():
    sys_in = sys.stdin
    sys_out = sys.stdout

    d = int(sys_in.readline())

    m = int(sys_in.readline())

    if d <= m:
        sys_out.write('0\n')
        sys.exit()

    n = int(sys_in.readline())

    stops1 = [0]

    stops2 = list(map(int, sys_in.readline().split()))
    stops1+=stops2

    stops1.append(d)


    sys_out.write(f'{get_stops(d, m, stops1, n)}\n')
    

if __name__ == '__main__':
    main()