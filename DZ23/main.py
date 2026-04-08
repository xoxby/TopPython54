import os

folders = [
    r"Work\F1",
    r"Work\F2\F21"
]

files_content = {
    r"Work\w.txt": "w text",
    r"Work\F1\f11.txt": "f11 text",
    r"Work\F1\f12.txt": "f12 text",
    r"Work\F1\f13.txt": "f13 text",
    r"Work\F2\F21\f211.txt": "f211 text",
    r"Work\F2\F21\f212.txt": "f212 text"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, text in files_content.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

print("Обход Work снизу вверх")
for root, dirs, files in os.walk("Work", topdown=False):
    print(root)
    print(dirs)
    print(files)

print("-" * 50)

print("Обход Work сверху вниз")
for root, dirs, files in os.walk("Work", topdown=True):
    print(root)
    print(dirs)
    print(files)
