import itertools as iter
# daily_data = list(iter.zip_longest(range(10), data)


def f(x):
    return x**2

ln1 = input()
ln1_list = ln1.split(" ")

input_data_dict = {}

for i in range(1,int(ln1_list[0])+1):
    x = input()
    input_data_dict[i] = x.split(" ")

#print(input_data_dict)

data_dict = {}

for k, v in input_data_dict.items():
    # print(f'{k}, {v}')
    new_list = []
    for i in v:
        new_list.append(int(i))
    data_dict[k] = sorted(new_list)
    data_list = list(iter.zip_longest(range(0,7), new_list))

print(data_dict)
#print(data_list)

for k, v in data_dict.items():
    for el in iter.product(v):
        print(el)

m = []
for k, v in data_dict.items():
    m.append(f(v[-1]))

#print(m, sum(m))

print(sum(m)%int(ln1_list[1]))