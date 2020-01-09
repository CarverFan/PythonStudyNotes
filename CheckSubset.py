
n = int(input())
cnt = 0
for i in range(n):
    num_of_elements1 = int(input())
    #print(num_of_elements1)
    set1 = set(input().split(" "))
    #print(set1)

    num_of_elements2 = int(input())
    #print(num_of_elements2)
    set2 = set(input().split(" "))
    #print(set2)

    if set1.issubset(set2):
        print(True)
    else:
        print(False)