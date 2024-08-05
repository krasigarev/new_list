fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for i in fruits:
    if "a" in i:
        new_list.append(i)

print(new_list)

new_list_2 = [x for x in fruits if "a" in x]
print(new_list_2)

new_list_2 = [x for x in fruits if x != "apple"]
print(new_list_2)

new_list_2 = [x for x in fruits]
print(new_list_2)

new_2 = [x for x in range(10 +1)]
print(new_2)

new_3 = [x for x in range(10) if x % 2 == 0]
print(new_3)

new_3 = [x for x in range(10) if x % 2 == 1]
print(new_3)

new_3 = [x for x in range(10) if x < 5]
print(new_3)

data_list = [x.upper() for x in fruits]
print(data_list)
data_list = [x.lower() for x in fruits]
print(data_list)
new_5 = ["banana" for x in fruits]
print(new_5)

new_6 = [x if x != "banana" else "orange" for x in fruits]
print(new_6)