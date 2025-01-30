"""Модуль для действий с csv файлами."""
# type: ignore
from __future__ import annotations

import os
import argparse
from pathlib import Path
import codecs
import sys


#
# Читает файл. Удаляет дубликаты строк указанных в параметрах.
#


WORD_SEPARATOR = ';'
SCRIPT_PATH = str(Path(__file__).absolute()).replace(Path(__file__).name, '', -1)


def split_line(line: str) -> list[str]:
    """Возвращает список элементов строки, прочитанной из файла."""
    return line.strip().split(WORD_SEPARATOR)

def read_lines_from_csv(filepath: Path) -> list:
    """Возвращает список строк CSV-файла, разеденных по разделителю."""
    with open(str(filepath), 'r', encoding='utf8') as f:
        result = f.readlines()

    if result:
        return [split_line(x) for x in result]
    
    return []


def write_to_csv(filepath, data):
    """Сохраняет строки в файл по указанному пути."""
    with codecs.open(str(filepath), 'w', encoding='utf-8') as f:
        f.writelines([f'{WORD_SEPARATOR.join(x)}\n' for x in data])


def init_params() -> argparse.ArgumentParser:
    """Возвращает объект для разбора входных параметров."""
    parser = argparse.ArgumentParser()

    parser.add_argument ('file1', type=str, help='main handling csv file')
    parser.add_argument ('-i', '--info', action='store_true', default=False, help='show info about main csv file')

    return parser

FILE_INFO = '''File info:
    columnes: %d
       lines: %d

     example: 
        "%s"
'''
def print_info(rows: list) -> None:
    """Выводит информацию о файле."""
    print(
        FILE_INFO % (
            len(rows[0]) if rows else 0,
            len(rows),
            f'{str(rows[:2])[0:-1]}...'
        )
    )


if __name__ == '__main__':
    parser = init_params()
    args = parser.parse_args()

    main_file_path = Path(args.file1)

    if not main_file_path.exists():
        print(f'handling file not found in path "{args.file1}"')
        sys.exit()
    
    if not main_file_path.suffix or main_file_path.suffix.lower() != '.csv':
        print(f'handling file extension not found or not a "csv": "{main_file_path.suffix}"')
        sys.exit()

    main_file_path_rows = read_lines_from_csv(args.file1)

    # Если никаких действий не указано, просто показываем информацию о файле.
    if not any([]):
        print_info(main_file_path_rows)

    if args.info:
        print_info(main_file_path_rows)

    
