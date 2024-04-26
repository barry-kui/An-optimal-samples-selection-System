import os
import sys
def file_display():
    file_path = f"./Data/45-7-4-3-3-1-14.txt"
    with open(file_path, "r") as file:
        file_lines = file.readlines()
        file_lines = [line.strip() for line in file_lines]
        for line in range(len(file_lines)):
            optimal_value = f"{line + 1}: {file_lines[line]}"
            print(optimal_value)
file_display()