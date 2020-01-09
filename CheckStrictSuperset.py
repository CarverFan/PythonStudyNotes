
superset = set(input().split(" "))
no_of_sets = int(input())
dict_of_sets = {}

for i in range(no_of_sets):
    dict_of_sets[i] = set(input().split(" "))

torf = []
for sets in dict_of_sets.values():
    if superset.issuperset(sets):
        torf.append(1)
    else:
        torf.append(0)

if 0 in torf:
    print(False)
else:
    print(True)

