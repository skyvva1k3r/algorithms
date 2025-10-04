import sys


def main():
    n = input().split()
    n, k = int(n[0]), int(n[1])
    prec = 0
    recall = 0
    codes = ["BIG", "BAG", "BUG", "BG", "UG"]

    for i in range(n+k):
        temp = input()
        flag = False
        j = 0
        while j != len(temp):
            temp=list(temp)
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
        if len(temp) <= 4:
            if int(temp[0]) > 2 and len(temp[0]) < 2:
                if temp[1] == "-":
                    if len(temp[2]) == 4 and temp[2].isnumeric():
                        if temp[3] in codes:
                            if temp[0] == "5" and (temp[3]=="BIG" or temp[3] == "BAG"):
                                pass
                            else:
                                recall += 1
                                if i <= k:
                                    prec += 1
    print(f"{prec/recall}".ljust(6, "0"),"\n",f"{prec/n}".ljust(6, "0"), sep = "")




if __name__ == '__main__':
    main()
