# ***** Dictionary operations ******
my_dict = {'a' : 'Satyabrat', 'c': 'Rajesh', 'b': 'Sudhansu', 'd': 'Ravi'}
for k in my_dict.keys():
    print(k)

for k in sorted(my_dict.keys()):
    print(k, my_dict[k])


# ***** Dictionary Formatting ******
dict_to_format = {'word': 'garfield', 'count': 42}
message = 'I want %(count)d copies of %(word)s' % dict_to_format  # %d for int, %s for string
print(message)
