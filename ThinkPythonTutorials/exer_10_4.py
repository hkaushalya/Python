#Exercise 10-4.
#Write a function called 'middle' that takes a list and returns a new list
#that contains all but the first and last elements.

def middle(t):
    last = len(t)
    first = 0
    if (last>0): #there is something
        t.pop(last-1)

    if (len(t)>0): #still there is something
        t.pop(0)

    return t

mylist = [1,2,3,4]

print middle(mylist)
