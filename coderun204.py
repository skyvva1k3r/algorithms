import sys


def main():
    n, errors, summ = int(input()), [], 0
    for i in range(n):
        temp = [int(x) for x in input().split()]
        errors.append(((temp[0]/100)*temp[1]))
        summ += (((temp[0]/100)*temp[1]))
    for error in errors:
        print(round(error/summ, 12))

if __name__ == '__main__':
    main()
