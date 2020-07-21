from nltk import*
from nltk.corpus import*
from matplotlib import pyplot as plt

file = open("frankenstein_copy.txt")                        # open frankenstein text files
text = file.read().upper()                                  # make it all uppercase

people = []
      
file1 = open('names.txt')                                   
names = file1.read()
####################### TRACK A GIVEN CHARACTER IN A TEXT ##############################
list1 = text.split('CHAPTER')                               # separate out each chapter
new = []
cols = []
r = 1
g = .5
b = 0
a = 1
count = 0
for _ in range(len(list1)):                                 # get RGB values to make a pretty graph
    cols.append((r,g,b,a))
    r -= .02
    g += .01
    b += .02
for lst in list1:                                           # get the words in each chapter
    new.append(word_tokenize(lst))
name1 = input("Which character do you want to track? ")     # get name of character to track
name = name1.upper()
chapters = new
counts = [0] * len(chapters)
print(len(chapters))
for i in range(len(chapters)):                              # count the occurrences of the name in each chapter
    chapter = chapters[i]
    for word in chapter:
        if word == name:
            print(word)
            counts[i] += 1
            
chaps = []
print(counts)
for i in range(len(chapters)):                              # relabel the chapter names (starting from 1)
    chaps.append(i+1)
    
print(chaps)
plt.title("Tracking {} in Frankenstein".format(name1))      # give a title
plt.xlabel("Chapter")                                       # label axes
plt.ylabel("Number of Mentions")                            
plt.bar(chaps, counts, color=cols)                          # create the graph
plt.xticks(chaps, chaps)                                    # reassign the chapter numbers
plt.show()
####################### TRACK A GIVEN CHARACTER IN A TEXT ##############################
####################### TRACK PARTS OF SPEECH IN A TEXT ##############################

tokens = word_tokenize(text)                                # break into words
types = pos_tag(tokens)                                     # part of speech tag
proper = []
pos_list = []
for item in types:                                          # get the unique parts of speech
    if item[1] not in pos_list:
#        print(item[1])
        pos_list.append(item[1])

bins = pos_list
counts = [0] * len(pos_list)
for word in types:                                          # get counts for each part of speech
    loc = pos_list.index(word[1])
    counts[loc] += 1

    
# PARTS OF SPEECH
loc = 0
plt.title("Frequencies of the Parts of Speech In Frankenstein") #title the graph
plt.xlabel("Parts of Speech")                                   # label x axis
plt.ylabel("Number of Occurrences")                             # label y axis
cols = []
r = 1
g = .5
b = 0
a = 1
locs = []
count = 0
for _ in range(len(bins)):                                      # get RGB values to make a pretty graph
    cols.append((r,g,b,a))
    locs.append(count)
    count+=8
    r -= .02
    g += .01
    b += .02
    
plt.bar(locs, counts, color=cols, width=6)                      #create graph
plt.xticks(locs, labels=bins, rotation='vertical', size='small')    # relabel the markings on the x axis
plt.show()
####################### TRACK PARTS OF SPEECH IN A TEXT ##############################

########################## MISCELLANEOUS/GARBAGE CODE BELOW THIS POINT ########################################

loc = 0
for i in range(len(bins)):
#    print(bins[i])
    plt.bar([loc], [counts[i]], align='center', color=cols[i], label=bins[i], width=5)
    loc += 8
    
plt.xticks(locs, labels=bins, rotation='vertical', size='small')
#plt.show()


buckets = []
temp = ""
for char in names:
    if char in ["\n"]:
        buckets.append(temp)
        temp = ""
    else:
        temp += char
buckets.append(temp)
new = []
for bucket in buckets:
    if bucket[-1] in [" ", "\t", "\n"]:
        new.append(bucket[:-1])
    else:
        new.append(bucket)
buckets = new
#for bucket in buckets:
#    print('start:', bucket, ':end', sep="")
#for bucket in buckets:
#    if bucket not in ["\n"]:
#        new.append(bucket)
#        print('start:', bucket, ':end', sep="")
#buckets = new


for item in types:
    if item[1] == 'NNP':
        proper.append(item[0])
        
#print(proper)
# TRACKING USE OF ELIZABETH
chapters = []
line = []
for item in proper:
    if item.upper() == "CHAPTER":
        chapters.append(line)
        line = []
    if item.upper() == "ELIZABETH":
        line.append(item)
chapters.append(line)
new = []
for chapter in chapters:
    if chapter != []:
        new.append(chapter)
chapters = new
#print(chapters)
char_counts = [0] * len(chapters)
for i in range(len(chapters)):
    char_counts[i] += len(chapters[i])

new = []
r = 0
g = 1
b = 0
a = .5
locs = []
counter = 0
nums = []
num = 1
for _ in range(len(chapters)):
    new.append((r,g,b,a))
    nums.append(num)
    locs.append(counter)
    num += 1
    r += .3
    g -= .3
    b += .3
    counter += 6
loc = 0

for i in range(len(chapters)):
    plt.bar([loc], [char_counts[i]], align='center', color=new[i], width = 5)
    loc += 6
plt.title("Elizabeth's Appearances in Frankenstein")
plt.xlabel("Chapter")
plt.ylabel("Number of Appearances")
plt.xticks(locs, labels=nums, size='small')
#plt.show()
proper_chapters = []
line = []
for item in proper:
#    if item == "Alphonse":
#        print("ITEM: {}".format(item))
    if item == "Chapter":
        proper_chapters.append(line)
        line = []
    if item in buckets:
 #       print(item)
        line.append(item)
proper_chapters.append(line)
real = []
for chapter in proper_chapters:
    if chapter != []:
        real.append(chapter)

counts = [0] * len(buckets)
for chapter in real:
    for i in range(len(chapter)):
        name = chapter[i]
 #       if name == "Alphonse":
 #           print("ALPHONSE")
 #       print("NAME: {}".format(name))
        loc = buckets.index(name)
 #       print(loc)
        counts[loc] += 1
#for i in range(len(buckets)):
#    print("BUCKET: {} COUNT: {}".format(buckets[i], counts[i]))
colors = []
r = 0
g = .5
b = 1
a = 1
for i in range(len(buckets)):
    colors.append((r,g,b))
    r += .02
    g += .02
    b -= .02

# TRACKING ALL CHARACTERS
plt.title("Character Frequencies in Mary Shelley's Frankenstein")
plt.xlabel('Characters')
plt.ylabel('Frequency')
loc = 0
for i in range(len(buckets)):
    plt.bar([loc], [counts[i]], align='center', color=colors[i],label=buckets[i],width=5)
    loc += 6
locs = []
count = 0
for _ in range(len(buckets)):
    locs.append(count)
    count += 6
plt.xticks(locs, labels=buckets, rotation='vertical')
#plt.show()


#colors = []
#r = g = b = 0
#for i in range(len(buckets)):
#    colors.append((r,g,b))
#    r += 20
#    g += 20
#    b += 20
#print(colors)


#fdist = FreqDist(tokens)
#fdist.plot(30, cumulative=False)
#plt.show()

#bins = pos_list
#counts = [0] * len(pos_list)
#for word in types:
#    loc = pos_list.index(word[1])
#    counts[loc] += 1
#print(len(bins))
#print(len(counts))
#loc = 0
#buckets = ['Negative', 'Neutral', 'Positive']
#colors = ['red', 'goldenrod', 'lawngreen']
#reqs = [len(negative_words), len(neutral_words),len(positive_words)]
#for freq in freqs:
#    print(freq)
#or i in range(len(buckets)):
 #   plt.bar([loc], [freqs[i]], align='center', color=colors[i], label=buckets[i], width=5)
# #   loc += 6
#plt.xlabel('Tone')
#plt.ylabel('Frequency')
#plt.title('Overall Tone in Letter 1: Frankenstein')
#plt.xticks([0, 6, 12], labels=buckets, rotation='vertical')
#plt.show()
#colors = ['c', 'm', 'r', 'b']
#cols = []
#for i in range(len(bins)):
#    cols.append(colors[i%4])
#for i in range(len(bins)):
#    plt.bar([loc],[counts[i]], align='center', label=bins[i],width=1)
#    loc+=1
#plt.xlabel('Parts of Speech')
#plt.ylabel('Frequency')
#print(bins)
#plt.title('Letter 1: Frankenstein')
#plt.xticks(range(len(bins)), labels=bins, rotation='vertical', size='small')
#plt.show()
#plt.pie(counts, labels=bins, colors = cols)
#plt.show()
#plt.title("Parts of Speech")
#stop_words = set(stopwords.words("english"))

#used_stops = []
#for word in types:
#    if word[0] in stop_words:
#        used_stops.append(word[0])
