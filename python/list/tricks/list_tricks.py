
##### Generators in Python #########
##### Generates values on fly, doesnt store in memory #######
##### Can be traversed only once #######
myGenerator = (x*x for x in xrange(50))

for x in myGenerator:
    print(x)
