
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
print (listNew[2])

# ***** Lists Insert [Appends after last element of list] ******
listNew = ['first_element', 'third_element']
listNew.insert(1, 'second_element')
print (listNew[1])

# ***** List sorting ******
alist = [24, 12, 30, 5, 24]
for x in sorted(alist, reverse=True):
    print x


# ***** List sorting with key ******
def find_maximum_number_of_a_chars(word):
    repeatedA = 0
    chars = list(word)
    for x in chars:
        if x == 'a' or x == 'A':
            repeatedA+1
    return repeatedA

word_list = ['Satyabrat', 'Ravishekher', 'Amit', 'Jonathan']
for x in sorted(word_list, key=find_maximum_number_of_a_chars):
    print x