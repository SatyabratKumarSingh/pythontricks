
# ******* Generators in Python **********
# ******* Generates values on fly, doesnt store in memory *******
# ******* Can be traversed only once ******
myGenerator = (x*2 for x in xrange(10))

for x in myGenerator:
    print(x)


# ****** Yields in Python *********
# ***** Creates a generator *******
# ***** Can be traversed only once ****
def createGenerator():
    mylist = xrange(5)
    for i in mylist:
        yield i*i
for x in createGenerator():
    print(x)


# ***** Lists Append [Appends after last element of list] ******
listNew = ['first object', 'second object']
listNew.append('third_element')
print (listNew[3])

# ***** Lists Insert [Appends after last element of list] ******
listNew = ['first_element', 'third_element']
listNew.insert(1, 'second_element')
print (listNew[1])
