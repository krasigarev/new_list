data_list = [1, 2, 3, 4, 5, 3]

print(max(data_list))
print(min(data_list))

print(data_list[:2])
print(data_list[:-1])

a = []

a.append(data_list)
print(a)
b = data_list.count(3)
print(b)
print(data_list.index(5))
data_list.insert(2, 11)
print(data_list)

data_list.pop(-1)
print(data_list)
a = data_list.pop(-1)
print(a)
data_list.remove(11)
print(data_list)
data_list.reverse()
print(data_list)
data_list.sort()
print(data_list)
data_list.sort(reverse=True)
print(data_list)

list_1 = []
n = int(input())
for i in range(n):
    list_1.append(int(input()))
    list_1 += [int(input())]

print(list_1)
