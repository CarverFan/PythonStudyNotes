import itertools as iter

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
new_list = []
for k, v in input_data_dict.items():
    # print(f'{k}, {v}')
    for i in v:
        new_list.append(int(i))

#print(new_list)

squares = list(map(f, new_list))
print(squares)

for k, v in data_dict.items():
    for el in iter.product(v):
        print(el)


print(sum(m)%int(ln1_list[1]))