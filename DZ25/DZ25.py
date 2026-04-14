import json
from pathlib import Path


JOURNAL_FILE = Path(__file__).with_name("journal.json")


def add_student(journal, name, grades):
    journal.append({"name": name, "grades": grades})


def average_grade(grades):
    if not grades:
        return 0
    return round(sum(grades) / len(grades), 2)


def save_journal(path, journal):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(journal, file, ensure_ascii=False, indent=2)


def load_journal(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_report(journal):
    print("Журнал успеваемости")
    print("-" * 50)
    for item in journal:
        name = item["name"]
        grades = item["grades"]
        avg = average_grade(grades)
        print(f"{name:12} | оценки: {grades} | средний балл: {avg}")


students_journal = []
add_student(students_journal, "Анна", [10, 11, 12, 9])
add_student(students_journal, "Олег", [8, 7, 9, 10])
add_student(students_journal, "Мария", [12, 12, 11, 12])

save_journal(JOURNAL_FILE, students_journal)
loaded_journal = load_journal(JOURNAL_FILE)
print_report(loaded_journal)
