import sys


def main():
    month = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday", "Saturday"]
    n = input().split()
    days, limit = int(n[0]), month.index(n[1])
    print(days, limit)
    a = 10
    for i in range(days//7):
        days -= 7
        print()
        for j in range(days%7):
            print(".", end = " ")
if __name__ == '__main__':
    main()