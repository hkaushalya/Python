count = 0
inthere = False

def inc():
    global count
    global inthere
    count += 5
    inthere = True

#fin = open("/Users/samantha/Documents/Personal/Samantha/Python_Tutorials/thinkPython_stuff/words.txt")
#wordlist = {}
#for line in fin:
#    word = line.strip()
#    wordlist[word] = 'NA'

#print wordlist
#print 'arg' in wordlist
#print 'goose' in wordlist
#print 'jawbone' in wordlist

print count,",", inthere
inc()
print count,",", inthere
inc()
print count,",", inthere
