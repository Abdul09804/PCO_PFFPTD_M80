# Regular Expression
"""
-> Here we write an expression to match the pattern and get the data from a huge file
-> To work with patterns we have to import a module called 're'
"""

import re

# Character
"""
. -> matches any character except new line 
\. -> matches a dot
\\ -> matches backslash
\* -> matches astrick
"""

# Character Set
"""
[abcd] -> matches either 'a' or 'b' or 'c' or 'd'
[^abcd] -> matches any character but not 'a' or 'b' or 'c' or 'd'
[234] -> matches '2' or '3' or '4'
[aeiouAEIOU] -> matches any vowel
[a-z] -> matches any lowercase character
[A-Z] -> matches any uppercase character
[0-9] -> matches numeric characters
[A-Za-z] -> matches any alphabet
[A-Za-z0-9] -> matches any alphanumeric
"""

# special characters
"""
\w -> word character, same as [a-zA-Z0-9_] -> matches alphanumeric and _
\W -> non word character, same as [^a-zA-Z0-9_] -> matches anything other than word character
\d -> matches a digit, same as [0-9]
\D -> matches a non-digit, same as [^0-9]
\s -> matches only whitespace
\s -> matches non white space
"""

# anchors
"""
^ -> start of string
$ -> end of string
\b -> word boundary
\B -> not a word boundary
[] -> matches characters in square brackets 
[^] -> matches characters not in square brackets
"""

# Quantifiers
"""
* ->  match expression 0 or more times
+ -> match expression 1 or more times
? -> matches 0 or 1 time
{min, max} -> matches atleast 'min' no of characters and almost 'max' characters
{num} -> matches exactly 'num' values
"""

# Grouping
"""
("A" | "B" | "C") -> Either "A" or "B" or "C"
"""

# word boundary (\b)
"""
-> start of the word is where sequence of alphanumeric characters begin
-> end of the word is where sequence of alphanumeric ends
Rule: The match that begins the earliest wins
Ex: 'abcda'
'cbabcdabcda'
"""

# functions
"""
re.findall(expression, string) -> returns a list of all the matches
"""

