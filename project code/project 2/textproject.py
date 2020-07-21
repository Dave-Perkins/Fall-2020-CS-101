import matplotlib.pyplot as plt
from os import path
from nltk import *
from nltk.corpus import *
import random

def get_file():
    """
    Function prompts user to enter a file name and checks if that file exists.
    If not, prompts user again until they enter a existing file.
    """
    # Main Loop
    while True:
        filename = input("Please enter the name of the file you want to work on: ")
        # Check if file exists...
        if path.exists(filename):
            print("File sucessfully retrieved. Returning to previous menu...")
            print()
            return filename
        
        print("That file does not exist in your current directroy. Try again.")
        print()

def remove_weirdness(strlist):
    """
    NLTK seems to have some issue with turning 's into â€™. This function removes that stuff
    """
    weirdness = 'â€™'
    result = []
    for string in strlist:
        check = string.find(weirdness)
        if check != -1:
            beginning = string[:check]
            end = string[check + 3:]
            string = beginning + '\'' + end
            
        result.append(string)
        
    return result

def stringprettify(strlist):
    """
    Formats a list of strings into a pleasent format.
    Also removes strange text as mentioned in remove_weirdness
    Doesn't work perfectly, but whatever.
    Returns the formated string
    """
    strlist = remove_weirdness(strlist)
    result = ""
    punc = [".", "!", "?", ":"]
    for index in range(len(strlist)):
        string = strlist[index]
        # If its not a punctuation or followed by a punctuation
        if string not in punc and strlist[index + 1] not in punc:
            result += string + " "
        # If we are not at the end of the string and
        # the index is followed by puncuation
        elif index + 1 < len(strlist) and strlist[index + 1] in punc:
            result += string
        else:
            result += string + "\n"
            
    return result
            
def get_words_for_fill(text, types_to_remove):
    """
    Function goes through a text and uses NLTK to tokenize it,
    grabbing all parts of speech contained in the
    types_to_remove list.
    Returns a List of lists of a part of speech (string) and a list of those words.
    """
    # Parts of speech parsing
    types = pos_tag(text)
    
    word_lst = []
    
    # For each type to remove, we append it and a list of words to word_lst
    for index in range(len(types_to_remove)):
        word_lst.append([types_to_remove[index], []])
    
    # For each tuple of PoS and word...
    for tups in types:
        word, pos = tups
        # Check if PoS is one we want...
        if pos in types_to_remove:
            check = types_to_remove.index(pos)
            # And add the word to the correct list
            word_lst[check][1].append(word)
            
    return word_lst
    

def madlib_remove(text, types_to_remove):
    """
    Function takes a text (List of strings) and removes a random amount of words that are
    parts of speech specified in types_to_remove_list
    
    Returns a new list of strings with some words removed and replaced by a string
    denoting thier parts of speech
    """
    # Tokenize the text
    tokens = word_tokenize(text)
    # Gets rid of weirdness
    tokens = remove_weirdness(tokens)
    # Gets parts of speech
    orignial = pos_tag(tokens)
    word_lst = []
    
    word_index = 0
    # next_remove is used along with word_index
    # to determine if we want to remove a word
    next_remove = random.randint(1, 5)        
        
    # While our counter (word_index) is less than the length of the text...   
    while word_index < len(orignial):
        # extract a word and its PoS
        word, pos = orignial[word_index]
        
        remove = False
        # If it's part of speech is one of the correct ones
        if pos in types_to_remove:
            target_type = True
        else:
            target_type = False
            
        # If word_index == next_remove, then we want to remove this word,
        if word_index == next_remove:
            # But only if it's of the correct PoS
            if target_type:
                remove = True
                # If it is, we want to increment next_remove a little bit more,
                # So we don't remove a bunch of words in a row
                next_remove += random.randint(3, 6)
            else:
                # If it's not of the correct type, we increment next_remove
                # more slowly, so we can hopefully find the next word that is of
                # the correct part of speech
                next_remove += random.randint(1, 2)
        
        # And lastly if we want to remove the word, we append it's PoS, and if not,
        # we append it's word
        if remove:
            word_lst.append(pos)
        else:
            word_lst.append(word)
            
        # Increment Counter
        word_index += 1
        
    
    return word_lst
    
    
def fill_in_words(mad_lib, words, types):
    """
    Function takes a mad_lib generated by madlib_remove,
    words, which is list of lists of parts of speech and words generated by get_words_for_fill,
    and a list of types (parts of speech) that we remove and replace.
    
    Function then replaces those parts of speech place holders with
    words that match those parts of speech from the word list
    
    Returns a new list of strings with the PoS placeholders replaced
    with new words
    """
    result = []
    # For word in the text...
    for word in mad_lib:
        # If it's a place holder...
        if partofspeech in types:
            # Go through each PoS in the word list...
            for inner_index in range(len(words)):
                # Once you find the correct PoS...
                if words[inner_index][0] == partofspeech:
                    # Choice a random word from it's list
                    to_append = random.choice(words[inner_index][1])
                    
        else:
            # If it's not placerholder, then just append the word
            to_append = word
        
        result.append(to_append)
    
    return result
                    
    

def mad_libs():
    """
    Function for the interface for creating and filling in madlibs
    """

    # The parts of speech we are intrested in removing and replacing
    to_replace = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS"]
    done = False
    while not done:
        print("You're in the madlibs menu")
        print("Here are your options:")
        print("(1) Enter a file")
        print("(2) Enter a text")
        print("(3) Produce a mad lib from file")
        print("(4) Fill in a mad lib using a text")
        user_in = input("Choose an option by entering it's text. " \
                            "To exit enter nothing: ")
        print()
        
        if user_in.upper() == "ENTER A FILE":
            # Gets the text to turn into a madlib
            madlib_file = open(get_file())
            madlib_text = madlib_file.read()
            
        elif user_in.upper() == "ENTER A TEXT":
            # Gets a text from the gutenburg libary to get a bunch of words
            # we could use to replace words in the madlibs with.
            replacement_txt = input("Please enter the name of a text for words: ") + ".txt"
            replacement_txt = corpus.gutenberg.words(replacement_txt)
            fill_words = get_words_for_fill(replacement_txt, to_replace)
            
        elif user_in.upper() == "PRODUCE A MAD LIB FROM FILE" or \
             user_in.upper() == "PRODUCE MAD LIB":
            # Produces the madlib by removing a random amount of certain words
            # Outputs the madlib
            madlib_text = madlib_remove(madlib_text, to_replace)
            print(stringprettify(madlib_text))
             
        elif user_in.upper() == "FILL IN A MAD LIB USING A TEXT" or \
             user_in.upper() == "FILL IN MAD LIB":
            # Fills in the madlib with words from the text from
            # the gutenburg library. 
            # For example, austen-persuasion gives you
            # Jane Austen's Persuasion.
            # Outputs the filled-in madlib
            result = fill_in_words(madlib_text, fill_words, to_replace)
            print(stringprettify(result))
        elif user_in == "":
            # Exit the menu
            done = True
        else:
            print("Input not recognized! Please enter a valid input.\n")

def charecter_tracking():
    """
    Empty Function: In practice students would have other menu options to do,
                    but for examples, we split the work and only did one each.
    """
    pass
    

def main():
    """
    Main function for program. Implements the text analysis interface that
    allows users to use NLTK to analyize some text. In this program,
    the user can create and fill in madlibs.
    """
    
    
    print("Welcome to the text analysis software!")
    print()
    done = False
    
    while not done:
        # Main Loop
        print("You're in the root menu")
        print("Here are your options:")
        print("(1) Madlibs")
        print("(2) Option 2")
        user_in = input("Choose an option by entering it's text. " \
                            "To exit enter nothing: ")
        print()
    
        if user_in.upper() == "MADLIBS":
            mad_libs()
        elif user_in.upper() == "OPTION 2":
            print("2")
        elif user_in == "":
            # Exit
            done = True
        else:
            print("Input not recognized! Please enter a valid input.\n")


if __name__ == "__main__":
    main()