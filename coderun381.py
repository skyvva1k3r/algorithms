import sys

def main():
    month = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    n = input().split()
    days, weekday, temp = int(n[0]), month.index(n[1]), []
    for i in range(((days+6+weekday)//7)):
        temp = []
        for j in range(7):
            if i*7+j-weekday+1 > days: 
                break
            if i*7+j < weekday:
                temp.append("..")
            else:
                temp.append(f"{i*7+j-weekday+1}".rjust(2, "."))
        print(*temp)


if __name__ == '__main__':
    main()