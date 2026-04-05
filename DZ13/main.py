people = [("Иван", 25), ("Мария", 23), ("Петр", 25), ("Анна", 23)]

age_dict = {}
for name, age in people:
    if age in age_dict:
        age_dict[age].append(name)
    else:
        age_dict[age] = [name]

print(age_dict)


nums = [1, 1, 1, 2, 2, 3]
k = 2

count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

result = []
for i in range(k):
    result.append(sorted_items[i][0])

print(result)


dict1 = {
    1: {"name": "Иван", "age": 17},
    2: {"name": "Максим", "age": 27},
    3: {"name": "Петр", "age": 30}
}

dict2 = {
    2: {"name": "Мария", "age": 20},
    4: {"name": "Анна", "age": 22}
}

merged = {}
merged.update(dict1)
merged.update(dict2)

filtered = {k: v for k, v in merged.items() if v["age"] >= 18}

print(filtered)
