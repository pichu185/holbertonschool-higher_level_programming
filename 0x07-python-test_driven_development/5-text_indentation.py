#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """splits a text with "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    chars = 0
    for i in text:
        if chars == 0:
            if i == " ":
                continue
            else:
                chars = 1
        if chars == 1:
            if i == "?" or i == "." or i == ":":
                print(i)
                print()
                chars = 0
            else:
                print(i, end="")
