data_list = [2, 3, 6, 5, 8, 8, 4, 6, 7, 9]

data_list.append(11)
print(data_list)

new_list = ["bee", "moth"]
new_list.extend(["ant", "fly"])
print(new_list)

new_list.insert(1, "pork")
print(new_list)

new_list.remove("ant")
print(new_list)

new_list.pop()
print(new_list)
new_list.pop(1)
print(new_list)
print(data_list.index(3))
print(data_list.index(3, 1))
print(data_list.count(8))
data_list.sort()
print(data_list)
data_list.sort(reverse=True)
print(data_list)
data_list.reverse()
print(data_list)
data_list.copy()
new_list.append(data_list)
print(new_list)
print(len(new_list))