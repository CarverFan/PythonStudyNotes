if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    arr = list(dict.fromkeys(arr))
    print(arr[-2])