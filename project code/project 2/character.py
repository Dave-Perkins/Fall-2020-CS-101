from nltk import*
from nltk.corpus import*
from matplotlib import pyplot as plt


#takes a character name and a text(in the form of a string not a file) and returns
#a list of numbers which each unumber is the Nth word in the text
def character_word(character, words):
    wordPlaces = []
    for wordNum in range(len(words)):
        if words[wordNum] == character:
            wordPlaces.append(wordNum)
    return wordPlaces

#testing matplotlib
def tempf():
    x1 = [1,2,3,4,5]
    y1 = [1,2,3,4,5]
    x2 = [1,2,3,4,5]
    y2 = [5,4,3,2,1]

    plt.scatter(x1,y1)
    plt.scatter(x2,y2)
    plt.show()

#using king lear find the occances of a few charcters and plots the in a way
#that it is obvious where each character appeared over the course of the text
#and whihc characters overlaped
def main():
    file = open("lear.txt")
    textStr = file.read()

    tokens = word_tokenize(textStr)
    types = pos_tag(tokens)

    #gets the lists of occuraces
    learSpots = character_word("Lear", tokens)
    KentSpots = character_word("Kent", tokens)
    cordSpots = character_word("Cordelia", tokens)
    gloSpots = character_word("Gloucester", tokens)
    edSpots = character_word("Edgar", tokens)
    gonSpots = character_word("Goneril", tokens)

    #plots all these lists
    plt.scatter(learSpots,[1]*len(learSpots),label="Lear")
    plt.scatter(KentSpots,[2]*len(KentSpots),label="Kent")
    plt.scatter(cordSpots,[3]*len(cordSpots),label="Cordelia")
    plt.scatter(edSpots,[4]*len(edSpots),label="Edgar")
    plt.scatter(gloSpots,[5]*len(gloSpots),label="Gloucester")
    plt.scatter(gonSpots,[6]*len(gonSpots),label="Goneril")
    plt.legend()
    plt.title('Character Occurrence by Page Number')

    plt.show()


if __name__ == "__main__":
    main()
