import os


def main():
    fin = open('TheSandmansHour.txt')
    nlines = 0
    for line in fin:
        #print line
        nlines = nlines + 1

    print 'Lines in the book = ' , nlines



main()
