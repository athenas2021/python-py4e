# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one oar more times
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
total = 0
lista = list()
for item in handle:
  lista += (re.findall('[0-9]+', item))

for item in lista:
  total += int(item)

print(total)