lst = [3, 7, 2, 5, 2, 8, 3, 9, 5, 1, 7, 4, 3, 6, 1]
print("Исходный список:", lst)

clean = []
for item in lst:
    if lst.count(item) == 1 and item not in clean:
        clean.append(item)

print("Очищенный список:")
print(clean)

print("\nСортировка по возрастанию (без sort()):")
sorted_list = clean.copy()
for i in range(len(sorted_list)):
    for j in range(i + 1, len(sorted_list)):
        if sorted_list[i] > sorted_list[j]:
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

print(sorted_list)
