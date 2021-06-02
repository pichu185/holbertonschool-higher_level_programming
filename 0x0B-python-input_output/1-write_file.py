#!/usr/bin/python3

def write_file(filename="", text=""):
    with open("my_first_file.txt", mode="w", encoding="utf-8") as file:

        file.write("Holberton School is so cool!\n")
        
        for i in file:
            print i+=
