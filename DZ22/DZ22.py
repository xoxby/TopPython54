def swap_lines(filename, pos1, pos2):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    lines[pos1], lines[pos2] = lines[pos2], lines[pos1]
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def reverse_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    lines.reverse()
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def join_files(file1, file2, file3):
    with open(file1, 'r', encoding='utf-8') as f1:
        content1 = f1.read()
    with open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()
         
    with open(file3, 'w', encoding='utf-8') as f3:
        f3.write(content1)
        f3.write(content2)

with open("test1.txt", "w", encoding="utf-8") as f:
    f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")

swap_lines("test1.txt", 1, 2)
reverse_lines("test1.txt")

with open("part1.txt", "w", encoding="utf-8") as f:
    f.write("Первый файл.\n")
with open("part2.txt", "w", encoding="utf-8") as f:
    f.write("Второй файл.")
    
join_files("part1.txt", "part2.txt", "result3.txt")
