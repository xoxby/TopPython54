# -*- coding: utf-8 -*-
"""ДЗ №24: инспектор пути — os.path, datetime. Путь: аргумент CLI или input()."""
import os
import sys
from datetime import datetime


def _human_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} Б"
    kb = size_bytes / 1024
    if kb < 1024:
        return f"{size_bytes} Б ({kb:.2f} КБ)"
    mb = kb / 1024
    return f"{size_bytes} Б ({kb:.2f} КБ, {mb:.2f} МБ)"


def main() -> None:
    if len(sys.argv) > 1:
        path = sys.argv[1].strip()
    else:
        path = input("Введите путь: ").strip()

    if not path:
        print("Путь не задан.")
        return

    if not os.path.exists(path):
        print("Указанный путь не существует.")
        return

    absolute = os.path.abspath(path)

    if os.path.isfile(path):
        kind = "Файл"
    elif os.path.isdir(path):
        kind = "Директория"
    else:
        kind = "Особый объект"

    block = [
        "=" * 42,
        " ИНФОРМАЦИЯ О ПУТИ",
        "=" * 42,
        f"Абсолютный путь: {absolute}",
        f"Тип: {kind}",
    ]

    if os.path.isfile(path):
        size_b = os.path.getsize(path)
        block.append(f"Размер: {_human_size(size_b)}")
        mtime = os.path.getmtime(path)
        when = datetime.fromtimestamp(mtime).strftime("%d.%m.%Y %H:%M:%S")
        block.append(f"Время последнего изменения: {when}")

    block.append("=" * 42)
    print("\n".join(block))


if __name__ == "__main__":
    main()
