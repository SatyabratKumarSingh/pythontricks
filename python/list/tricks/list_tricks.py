# ******* Generators in Python **********
# ******* Generates values on fly, doesnt store in memory *******
# ******* Can be traversed only once ******
myGenerator = (x * 2 for x in xrange(10))

for x in myGenerator:
    print(x)


# ****** Yields in Python *********
# ***** Creates a generator *******
# ***** Can be traversed only once ****
def createGenerator():
    mylist = xrange(5)
    for i in mylist:
        yield i * i


for x in createGenerator():
    print(x)

# ***** Lists Append [Appends after last element of list] ******
list_new = ['first object', 'second object']
list_new.append('third_element')
print (list_new[2])

# ***** Lists Insert [Appends after last element of list] ******
listNew = ['first_element', 'third_element']
listNew.insert(1, 'second_element')
print (listNew[1])

# ***** List sorting ******
a_list = [24, 12, 30, 5, 24]
for x in sorted(a_list, reverse=True):
    print x


# ***** List sorting with key ******
def find_maximum_number_of_a_chars(word):
    repeated_a_char = 0
    chars = list(word)
    for x in chars:
        if x == 'a' or 'A' == x:
            repeated_a_char += 1
    return repeated_a_char


word_list = ['Satyabrat', 'Ravishekher', 'Amit', 'Jonathan']
for x in sorted(word_list, key=find_maximum_number_of_a_chars):
    print x

# ***** Sort method, doesnt create a new list, its faster ******
word_list.sort()
# cant write sorted_list = word_list.sort()

# Filter list
# *** Filter numbers less than or equal to 10
nums = [20, 8, 10, 6, 50, 60, 40, 14, 30]
for x in [n for n in nums if n <= 10]:
    print(x)

# *** Select names containing 'y'
names_list = ['Satyabrat', 'Ravishekher', 'Amit', 'Jonathan', 'XYZ']
for name in [single_name for single_name in names_list if 'y' in single_name.lower()]:
   print(name)

# *** Delete elements from a list
a_big_list = [12, 25, 17, 18, 19, 20, 21, 22, 23, 24, 25]
del a_big_list[-2:] # Delete last 2 elements
print a_big_list

del a_big_list[:2] # Delete first 2 elements
print a_big_list
