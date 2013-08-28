#think_python.pdf
#Exercise:9.2, 9.3
#learning to read in a file and manipulate the words
#to find which words has(not) given set of character.
#Finally, find out a list of 5 letters that would
#exclude least amount of words
#Aug. 25th. 2013
#@Author: Sam

import os
import operator

#how many words uses all the letter given by a string
def uses_all(wd, ltrs):
    for ltr in ltrs:
        times = wd.count(ltr)
        if times == 0:
            return False
    return True

def uses_all_main(fin):
    nwords = 0
    for line in fin:
        word = line.strip()
        #print word
        nwords += 1
        search_string='aeiou'
        wordswith_string = 0
        if uses_all(word, search_string):
            wordswith_string = wordswith_string + 1

    print 'Number of words with "', wordswith_string, ' = ' , wordswith_string




def has_e(wd):
    for char in wd:
        #print char
        if (char == 'e') or (char == 'E'):
            #print "E found"
            return True

    return False

def has_forbidden(wd, excl):
    for char in wd:
        for ex in excl:
            if (char == ex):
                excl[char] = excl[char] + 1
                return True

    return False

#a function that finds the five letters that would
#exclude the least number of words
def avoids(fin):
    #to find five letters with least numbers of words can be excluded
    smlltrs = map(chr, range(97,123)) #to get abcd.. quickly
    #capltrs = map(chr, range(65,91))
    #allltrs = smlltrs+capltrs
    nwords = 0
    #define a dictionary to count each letter occurance in every word
    mydic = {}
    for ltr in smlltrs:
        mydic[ltr] = 0

    print mydic

    for line in fin:
        word = line.strip()
        #print word
        nwords += 1
        has_forbidden(word, mydic)
        #print(word, "-> Has E/e?(",has_e(word),')-> Had ', badltrs, '?', has_forbidden(word,badltrs))
        #print word , has_forbidden(word, mydic)

    print 'nwords = ', nwords
    print '==== Number of words with each of the letters ====='
    print mydic
    #items = mydic.items()
    #print items
    #items.sort()
    #print items
    sorted_x = sorted(mydic.iteritems(), key=operator.itemgetter(1))
    print '=== Sorted from least occured to highest ==='
    print sorted_x
    #5 letters that would exclude the least amount of words
    print '**** The 5 letters that would exclude the least amount of words are ****'
    i = 0
    for key,val in sorted_x:
        print key,'->',val
        i = i + 1
        if i>4:
            break




def main():
    os.chdir("/Users/samantha/Documents/Personal/Samantha/Python_Tutorials/thinkPython_stuff")
    print os.getcwd()
    fin=open('words.txt')
    #print fin
    #line = fin.readline()
    #word = line.strip()
    #print line
    #print word

    #avoids(fin)
    uses_all_main(fin)

main()
