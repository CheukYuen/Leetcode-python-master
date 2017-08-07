import re

# + :1 or more
# * :0 or more
# ? :0 or 1


# . : any single characters except newline '\n'


# Greedy vs Non-Greedy
str = ':;lint:;code:;love:;you'

print str.find(':;')


#
# if match:
#     print 'found:"', match.group(), '"'
# else:
#     print 'did not find'


print ':;'.join(["4::lint", "code", "love", "you"])
