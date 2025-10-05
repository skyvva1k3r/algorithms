import sys


def main():
    n = input().split()
    n, k = int(n[0]), int(n[1])
    nums = ["2", "3", "4", "5", "6", "7", "8", "9"]
    codes = ["BIG", "BAG", "BUG", "BG", "UG"]
    prec, rec = 0, 0

    for i in range(n+k):
        temp = input()
        flag = False
        j = 0
        temp=list(temp)
        while j != len(temp):
            if temp[j].isnumeric() and flag:
                temp.insert(j, "/")
                flag = False
                j += 1
            elif not temp[j].isnumeric() and not flag:
                flag = True
                temp.insert(j, "/")
                j += 1
            else:
                j += 1
        temp ="".join(temp)
        temp = temp.split("/")
        if len(temp) == 4 and temp[0] in nums and temp[1] == "-" and len(temp[2]) == 4 and temp[2].isdigit() and int(temp[2]) > 0 and temp[3] in codes:
            if not (temp[0] == "5" and (temp[3] == "BIG" or temp[3] == "BAG")):
                if i < n:
                    prec += 1
                rec += 1
    recall = prec / n if n else 0.0
    precision = prec / (rec) if (rec) else 0.0

    print(f"{recall:.4f} {precision:.4f}")

if __name__ == '__main__':
    main()
