this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

data_list = ["apple", "banana", "cherry", "orange", "beans"]
data_list[1:3] = ["watermelon"]
print(data_list)

data_list.insert(2, "strawberry")
print(data_list)

del data_list[1]
print(data_list)

this_is_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

for x in this_is_list:
    print(x)

for i in range(len(this_is_list)):
    print(this_is_list[i])

i = 0
while i < len(this_is_list):
    print(this_is_list[i])
    i += 1

[print(x) for x in data_list]