"""
Iterators and iterables
"""
import itertools

n_length_of_list = int(input())
n_space_sep_list = input()
k_indices = int(input())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# create dict to give letters their corresponding value
joint_dict = {}
alphabet_nums = []
for i, j in enumerate(alphabet, 1):
    joint_dict[j] = i
# print(joint_dict)

n_list = n_space_sep_list.split(" ")
n_list_nums = []
for i in n_list:
    n_list_nums.append(joint_dict[i])
print(n_list_nums)

combinations = itertools.combinations(n_list_nums, k_indices)

comb_list = [result for result in combinations]
print(comb_list)
print([1 for x in comb_list if 1 in x])
result = sum([1 for x in comb_list if 1 in x]) / len(comb_list)
print('{}'.format(result))