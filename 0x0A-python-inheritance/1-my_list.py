#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
    
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
        