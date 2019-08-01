#!/usr/bin/env python3


def format_doc(code):
    # 格式化 function doc
    # 格式化 class doc
    is_function_define = False
    is_class_define = False

    results = []
    for line in code.splitlines():
        if line.count('"""') == 2 and (is_function_define or is_class_define):
            header, middle, end = line.split('"""')
            results.append(f'{header}"""{middle}\n{header}"""{end}')
        else:
            results.append(line)

        is_function_define = 'def ' in line
        is_class_define = 'class ' in line

    return '\n'.join(results).strip()


if __name__ == '__main__':
    target_file = 'example.py'

    target_lines = open(target_file).read()
    format_result = format_doc(target_lines)
    open(target_file, 'w').write(format_result)
