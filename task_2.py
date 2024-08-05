values = input()
items = values.split(" ")

nums = []

for i in items:
    nums += [int(i)]

print(nums)

nums_1 = [int(item) for item in input().split(" ")]
print(nums_1)

data_list = ["one", "two", "three", "four", "five", "six"]
for i in data_list:
    print(" ".join(i))
