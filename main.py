from __future__ import annotations
from pathlib import Path

#
# Читает 2 файла. Ищет элементы первого столбца из первого файла в элементах из
# первого столбца второго файла. При совпадении строки сохраняем в список 1, при
# несовпадении во второй. После поиска, записывает каждый список в свой 
# результирующий файл.
#


CHAR_SEPARATOR = ';'
SCRIPT_PATH = str(Path(__file__).absolute()).replace(Path(__file__).name, '', -1)


def split_line(line) -> list[str]:
    """Возвращает список элементов строки, прочитанной из файла."""
    return line.strip().split(CHAR_SEPARATOR)


def read_lines_from_csv(filepath: Path) -> list:
    """Возвращает список строк CSV-файла, разеденных по разделителю."""
    with open(str(filepath), 'r', encoding='utf8') as f:
        result = f.readlines()

    if result:
        return [split_line(x) for x in result]
    
    return []


def sort_lines_to_lists_by_key_matched(file_a_lines_data: list, file_b_lines_data: list) -> tuple[list[str], ...]:
    """
    Возвращает списки строк из первого CSV-файла.
    
    В первом списке содержатся строки с совпадением по ключу со вторым файлом,
    во втором все остальные.
    """
    rows_matched_by_key = []
    rows_not_matched_by_key = []
    for word in file_a_lines_data:
        if word in file_b_lines_data:
            rows_matched_by_key.append(file_a_lines_data[word])
        else:
            rows_not_matched_by_key.append(file_a_lines_data[word])
    
    return rows_matched_by_key, rows_not_matched_by_key


def write_to_csv(filepath, data):
    """Сохраняет строки в файл по указанному пути."""
    with open(str(filepath), 'w') as f:
        f.writelines([f'{CHAR_SEPARATOR.join(x)}\n' for x in data])


if __name__ == '__main__':
    file_a_path = Path(SCRIPT_PATH) / '1.csv'
    file_b_path = Path(SCRIPT_PATH) / '2.csv'

    file_a_data = {x[0]: x for x in read_lines_from_csv(file_a_path)}
    file_b_data = {x[0]: x for x in read_lines_from_csv(file_b_path)}

    matched_rows, not_matched_rows = sort_lines_to_lists_by_key_matched(file_a_data, file_b_data)
    
    write_to_csv(Path(SCRIPT_PATH) / 'пересекался.csv', matched_rows)
    write_to_csv(Path(SCRIPT_PATH) / 'непересекался.csv', not_matched_rows)
