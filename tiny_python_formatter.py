#!/usr/bin/env python3
import os
import sys


def format_doc(code):
    # 格式化 function doc
    # 格式化 class doc
    is_function_define = False
    is_class_define = False

    results = []
    for line in code.splitlines():
        if line.count('"""') == 2 and (is_function_define or is_class_define):
            header, middle, end = line.split('"""')
            results.append(f'{header}"""{middle.strip()}\n{header}"""{end}')
        else:
            results.append(line)

        is_function_define = 'def ' in line
        is_class_define = 'class ' in line

    result = '\n'.join(results).strip() + '\n'
    if result == '\n':
        return ''
    else:
        return result


def process_dir(target_dir):
    assert os.path.isdir(target_dir)

    for (path, dirs, files) in os.walk(target_dir):
        # 避免处理隐藏目录
        files = [_file for _file in files if not _file[0] == '.']
        dirs[:] = [_dir for _dir in dirs if not _dir[0] == '.']

        for _file in files:
            if _file[-3:] != '.py':
                continue

            target_file = os.path.join(path, _file)
            print(target_file)

            target_lines = open(target_file).read()
            format_result = format_doc(target_lines)
            open(target_file, 'w').write(format_result)


if __name__ == '__main__':
    process_dir(sys.argv[1])
