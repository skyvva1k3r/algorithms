import sys
from itertools import permutations

def main():
    l, n = map(int, input().split())
    result = 10**9
    splits = input().split()
    varis = []
    thread = [0, l]

    for p in permutations(splits):
        varis.append("".join(p))
    
    print(varis)

    for i in range(len(varis)):
        temp = 0
        for j in range(len(splits)):
            for k in range(len(thread)):
                if thread[k-1] < (l - int(varis[i][j])) and thread[k] > (l - int(varis[i][j])):
                    print(thread[k])
                    temp += thread[k]
                    break
            thread.append(int(varis[i][j]))
            thread.sort()
            print("\n\n\n", temp, thread, varis[i][j], "\n\n\n", sep = "\n")
        print("--------------------------------------------------------")
        thread = [0, l]
        if result > temp:
            result = temp
    print(result) 
  


if __name__ == '__main__':
    main()
