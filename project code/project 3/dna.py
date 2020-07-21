"""
DNA matching Project Example
Gwen Urbanczyk
"""
import math
import csv
import random


def get_files():
    """
    Prompts user for input for the filenames of the DNA database,
    and the text file containting the test strand.
    Does not use csv module for parsing csv.
    Returns a tuple of the parsed database, and the string of bases.
    """
    #csv_file = "dna.csv"
    #test_file = "testcase.txt"
    csv_file = input("Please enter the file for the DNA database: ")
    test_file = input("Please enter the file for the test strand: ")
    
    csv_file = open(csv_file).read().split('\n')
    test_file = open(test_file).read()
    
    for i in range(len(csv_file)):
        csv_file[i] = csv_file[i].split(',')
    
    return (csv_file, test_file)

def get_match(csv_file, test_file):
    """
    Function takes csv_file as a 2D-List, and test_file as a string of bases
    Function computes the longest run of each STR in the database for the test_file strand.
    It then checks those numbers against the ones in the database. If a match is found,
    the string of the person's name is returned. If there is no match, 'No Match' is returned.
    """
    test_counts = []
    
    # For each STR in the database
    for csv_index in range(1, len(csv_file)):
        count = 0
        maximum = 0
        # test_bases is the STR we are currently counting 
        test_bases = csv_file[0][csv_index]
        # Find the first instance of the current STR
        start_index =  test_file.find(test_bases)
        
        # Starting from the first occurance of the STR, check if the next 
        # n charecters, (where n is the length of the STR) matches the STR. If so,
        # add one to count(run length). Otherwise, check count against maximum,
        # replacing maximum with count if applicable, and reseting count to 0.
        # We then step by n, continuing along the string
        for test_index in range(start_index, len(test_file), len(test_bases)):
            if test_bases == test_file[test_index:test_index + len(test_bases)]:
                count += 1
            else:
                if maximum < count:
                    maximum = count

                count = 0
                
        # This edge case occurs when a substring run is at the end of a string.
        # If so, we never compare maximum to count, so that run is ignored
        # without this check
        if maximum < count:
            maximum = count

        # we then append the longest run of the STR to the test_counts list
        test_counts.append(str(maximum))
        
    # We then check each row in the file to check if the columns after
    # the first (the name) match test_counts. If so, we have a match,
    # and we return the first element of the row, which is the
    # match's name
    for csv_entry in csv_file:
        counts = csv_entry[1:]
        if counts == test_counts:
            # Exact Match, return name of match
            return csv_entry[0]
    
    # No Match

    return "No Match"


def main():
    """
    Main calls get_files() to get the file names from the user, open, and parse the files.
    It then calls get_match and output the results
    """
    csv_file, test_file = get_files()
    
    print(get_match(csv_file, test_file))
    


if __name__ == "__main__":
    main()