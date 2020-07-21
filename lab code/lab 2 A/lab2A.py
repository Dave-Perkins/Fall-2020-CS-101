"""
Lab 2A: Graphing Data and working with Language!
"""

import random
import matplotlib.pyplot as plt


# Don't touch this!!!
def open_data(filename):
    file = open(filename)
    
    lines = file.readlines()
    for index in range(len(lines)):
        line = lines[index]
        line = line.strip().split(',')
        lines[index] = line[1:]
        for index2 in range(len(lines[index])):
            lines[index][index2] = lines[index][index2].lower().strip('"')
    
    
    data = []
    
    for question in range(len(lines[0])):
        question_lst = []
        for line in lines[1:]:
            question_lst.append(line[question])
        
        data.append((lines[0][question], question_lst))
        
    return data

def main():
    data = open_data("CS101 Lab Survey.csv")
    
    # Start writing your code here!
    

if __name__ == "__main__":
    main()