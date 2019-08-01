#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tiny_python_formatter import format_doc


def test_format_doc():
    code = '''
def my_func():
    """my doc"""
    pass


class MyClass:
    """my doc class"""

    def __init__(self):
        """my doc func"""
        pass
'''
    assert format_doc(code) == '''def my_func():
    """my doc
    """
    pass


class MyClass:
    """my doc class
    """

    def __init__(self):
        """my doc func
        """
        pass'''


if __name__ == "__main__":
    test_format_doc()
