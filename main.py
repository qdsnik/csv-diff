from __future__ import annotations
import os
from os import path


def read_csv(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        result = f.readlines()

    if result:
        return [[*x.strip().split(';')] for x in result]
    
    return []


def write_to_csv(filepath, data):
    with open(filepath, 'w') as f:
        f.writelines([';'.join(x)+'\n' for x in data])


if __name__ == '__main__':
    f1_path = os.path.join(os.getcwd(), '1.csv')
    f2_path = os.path.join(os.getcwd(), '2.csv')

    file_a = {x[0]: x for x in read_csv(f1_path)}
    file_b = {x[0]: x for x in read_csv(f2_path)}

    matched_rows = []
    not_matched_rows = []
    for word in file_a:
        if word in file_b:
            matched_rows.append(file_a[word])
        else:
            not_matched_rows.append(file_a[word])
    
    write_to_csv(os.path.join(os.getcwd(), 'пересекался.csv'), matched_rows)
    write_to_csv(os.path.join(os.getcwd(), 'непересекался.csv'), not_matched_rows)
