import sys


def main():
    n = int(input())
    r, l, t, d, temp = 0,101 ,0, 101, []
    temp =(list(map(int, input().split())))
    r, l, t,d = temp[0], temp[0], temp[1], temp[1]
    for i in range(n-1):
        temp =(list(map(int, input().split())))
        if temp[0] > r: r = temp[0]
        if temp[0] < l: l = temp[0]
        if temp[1] > t: t = temp[1]
        if temp[1] < d: d = temp[1]
    print(l, d, r, t)

if __name__ == '__main__':
    main()
