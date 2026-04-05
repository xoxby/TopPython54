d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}

result = {}
result.update(d1)
result.update(d2)
result.update(d3)

print(result)


employees = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

print(employees['emp3'])
print(employees['emp3']['salary'])

employees['emp3']['salary'] = 8500

for key in employees:
    print(key)
    for field, value in employees[key].items():
        print(field, ":", value)


students_count = int(input("Количество студентов: "))
students = {}

for i in range(students_count):
    name = input(f"{i + 1}-й студент: ")
    score = int(input("Балл: "))
    students[name] = score

total = sum(students.values())
average = total / students_count

print(f"Средний балл: {average}. Студенты с баллом выше среднего:")

for name, score in students.items():
    if score > average:
        print(name)
