this_is_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_is_list.sort()
print(this_is_list)

data_num = [100, 50, 65, 82, 23, 1]
data_num.sort()
print(data_num)

data_num.sort(reverse=True)
print(data_num)


def my_func(n):
    return abs(n - 50)


data_num.sort(key=my_func)
print(data_num)

# Case Insensitive Sort

this_is_list.sort()
print(this_is_list)

this_list = ["apple", "Banana", "cherry", "Orange", "kiwi", "mango"]
this_list.sort()
print(this_list)

