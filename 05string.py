                              # string and string operation

''' A string is a sequence of characters. A character is simply a symbol.
    For example, the English language has 26 characters'''

# x ='aasim '
# print(type(x))

# string operation

# 1 string slicing

name='harry'
# print(name[0:1])
# print(name[0:2])
# print(name[0:3])
# print(name[0:4])
# print(name[0:5])
# print(name[:5])         # note these is equal to [0:5]
# print(name[3:])         # note the is equal to [3:5]
# print(name[4])
'''note String indexing in Python is zero-based: the first character in the string
has index 0 , the next has index 1 , and so on. The index of the last character
will be the length of the string minus one.
For any non-empty string s , s[len(s)-1] and s[-1] both return the last character.'''
#
# print(name[-1])  # note if length of the string is not given the we can find the last chracter by index -1
# print(name[-5])
# print(name[-4:-1])

# skipping the value
# str='amazing'
# print(str[0::2])

# important string function

# string='my name is aasim . nice to meet you'
#
# print(len(string))
# print(string.endswith('you'))
# print(string.count('a'))
# print(string.capitalize())
# print(string.find('m')) # it telss thast string is there or not and at which index
# print(string.replace('aasim','aasim khan'))


# escape sequence

# story= '0nce upon a time, there was a boy'
# print(story)
# story1=' once upon a time \nthere was a boy' # its use for creating a new line
# print(story1)
# #story3= '''0nce upon a time,
#         there was a boy'''    # it is also used for multi line
#
# story4=' once upon a time \\ there was a boy' # its use for putting backslash in code

# story5=' once upon a time \t there \" was a boy' # its use for putting backslash in code for putting a tab and quote
# print(story5)

