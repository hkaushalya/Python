#Exc. 13_2
#read in a text book and analyse the word frequency (word histogram)
#Print the 10 most frequented words

import string

debug = False
wordlist = {}
exclude = set(string.punctuation)

def most_common(wdlist):
    t = []
    for key,value in wdlist.items():
        t.append((value,key))

    t.sort(reverse=True)
    return t

def total_words(wdlist):
    return sum(wdlist.values())

def different_words(wdlist):
    return len(wdlist)

def process_word(wd):
    global wordlist
    #print 'got word = ', wd
    if wd in wordlist:
        wordlist[wd] += 1
    else:
        wordlist[wd] = 1

def process_line(line):
    global exclude
    for c in exclude:
        line = line.replace(c,"")

    cleanline = line.strip()
    words = cleanline.split()
    for word in words:
        wd = word.strip()
        process_word(wd.lower())


def read_file(filename):
    fin = open(filename)
    nlines = 0
    skip = True

    for line in fin:
        #print line
        nlines += 1
        if not skip:
            #%print line
            process_line(line)

        if 'CONTENTS' in line: #skip everything up to the contents page
            #print line
            skip = False

        if debug and nlines>1000:
            break


    print 'Read ', nlines , ' lines.'
    #print wordlist
    print 'Total words = ' , total_words(wordlist)
    print 'Different words = ' , different_words(wordlist)
    print '10 most common words= '
    t = most_common(wordlist)
    for freq, word in t[0:10]:
        print word ,'\t', freq



file1='/Users/samantha/Documents/Personal/Samantha/Python_Tutorials/thinkPython_stuff/TheSandmansHour.txt'
file2='/Users/samantha/Documents/Personal/Samantha/Python_Tutorials/thinkPython_stuff/LesMiserables.txt'
file3='/Users/samantha/Documents/Personal/Samantha/Python_Tutorials/thinkPython_stuff/TheAdventuresofSherlockHolmes.txt'
read_file(file1)
read_file(file2)
read_file(file3)
