import numpy as np

# my_array = np.array([[1, 2], [3, 4]])

# print(np.mean(my_array, axis = 0))
# print(np.mean(my_array, axis = 1))
# print(np.mean(my_array, axis = None))
# print(np.mean(my_array))

# print(np.var(my_array, axis = 0))
# print(np.var(my_array, axis = 1))
# print(np.var(my_array, axis = None))
# print(np.var(my_array))

# print(np.std(my_array, axis = 0))
# print(np.std(my_array, axis = 1))
# print(np.std(my_array, axis = None))
# print(np.std(my_array))

l1 = list(map(int, input().split()))

inner_list = []
for i in range(l1[0]):
    inner_list.append(list(map(int, input().split())))

# print(f'Inner List: {inner_list}')
a = np.zeros((0,l1[1]))
for i in inner_list:
    a = np.vstack([a, [i]])

# print(a)
# np.set_printoptions(legacy='1.13')
print(np.mean(a, axis = 1))
print(np.var(a, axis = 0))
print(np.std(a, axis = None))