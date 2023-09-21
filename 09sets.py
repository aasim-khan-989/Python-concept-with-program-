# sets in python
# creating a set
s = {1, 'aasim', 3+4j}
print(s)
print(type(s))
# creating an empty set
es = {}  # Wrong method
print(type(es))
emptyset = set() # write syntax of creating an empty set in python
print(type(emptyset))

# adding element to an empty
emptyset.add(1)
print(emptyset)

# note you can add only tuple in set

set=set()
set.add((1,2,3,4))
print(set)

# set methods or set
s1={1, 'a', 2, 3, 4, 'b'}
x2=s1.union({1, 'a', 2, 3, 5, 7, 4, 'b'})
print('::',x2)
print(':',s1.intersection({'aasim','sdf',4}))
print(len(s1))
s1.clear()
print(s1)
