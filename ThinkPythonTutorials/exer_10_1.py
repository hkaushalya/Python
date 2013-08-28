
def capitalize_all(t):
    res = []
    for x in t:
        res.append(x.capitalize())
    return res

######################
# This can handle nested list with upto depth of 1.
# i.e. a list inside a list.
# not beyond that, like , list in a list in a list!!!
######################
def capitalize_nested(t):
    res = []
    for x in t:
        #if len(x)>1:
        res += capitalize_all(x)
        #else:
        #    res += capitalize_all(x)
    return res


mylist = ['a','a','c']

nestedlist=['p','q',mylist,['x','y','z']
print capitalize_all(mylist)
print capitalize_nested(nestedlist)
