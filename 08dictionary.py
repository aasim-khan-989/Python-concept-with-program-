mydict = {'name': ' aasim',
          'surname': 'khan',
          'marks': [190, 120, 30],
          'another-dict': {'profile': 'sport', 'hobie': 'reading'},
          'tuple': ('a, b , c')
         }

print(mydict['name'])
print(mydict['marks'])
print(mydict['another-dict']['profile'])
print(mydict['tuple'])

mydict['marks'] = [130, 120, 20] # it can mutate it keys

# dictionary method

print(mydict.keys())  # it will create a dict-keys and list all the dict
print(type(mydict.keys()))
print(list(mydict.keys()))
print(mydict.values())

print(mydict.items()) # print all (key,values) in a dictionary

mydict.update({'a':[1,2,3]})
print(len(mydict))
print(mydict.get('vwa')) # it return none if key is not present and if returns the value  if key is present

