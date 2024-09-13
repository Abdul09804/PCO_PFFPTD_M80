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

print(re.findall("the", "the theory of relativity"))    # ['the', 'the']

print(re.findall("cat", "the fragging belly indicates your cat is too fat"))    # ['cat', 'cat']

print(re.findall("python", "python is a programming  language"))    # ['python']

print(re.findall("aeiou", "hello how are you"))     # []

print(re.findall(r"[aeiouAEIOU]", "Hello How are you"))     # ['e', 'o', 'o', 'a', 'e', 'o', 'u']


# match smith and Smith

print(re.findall(r"smith", "SilverSmith and Goldsmith"))    # ['smith']

print(re.findall(r"Smith", "SilverSmith and Goldsmith"))    # ['Smith']

print(re.findall(r"[sSmith]", "SilverSmith and Goldsmith"))     # ['S', 'i', 'S', 'm', 'i', 't', 'h', 's', 'm', 'i', 't', 'h']

print(re.findall(r"[sS]mith", "SilverSmith and Goldsmith"))     # ['Smith', 'smith']


# match seperate or separate
print(re.findall(r"sep[ae]rate", "separate and seperate"))      # ['separate', 'seperate']

# match gray or grey
print(re.findall(r"gr[ea]y", "grey and gray"))      # ['grey', 'gray']

# count vowels in a string
st = "python programming"
print(re.findall(r"[aeiou]", st))       # ['o', 'o', 'a', 'i']
print(len(re.findall(r"[aeiou]", st)))  # 4
print(''.join(re.findall(r"[aeiou]", st)))      # ooai

# match any number between 0 to 9
print(re.findall(r"[0123456789]", "The cost of 10 gram gold is 72345"))     # ['1', '0', '7', '2', '3', '4', '5']
print(re.findall(r"[0-9]", "The cost of 10 gram gold is 72345"))

# match html tags -> <h1>, <h2>, ............, <h6>
print(re.findall(r"<h[1-6]>", "<h1> <h2> <h3> <h4> <h5> <h6>"))     # ['<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>']

# match all lowercase characters
print(re.findall(r"[a-z]", "Hello WelCoMe to PytHon ClAsS"))

# match all uppercase characters
print(re.findall(r"[A-Z]", "Hello WelCoMe to PytHon ClAsS"))

# match both uc and lc
print(re.findall(r"[A-Za-z]", "Hello WelCoMe to PytHon ClAsS"))

# count the total number of alphabets
print(len(re.findall(r"[A-Za-z]", "Hello WelCoMe to PytHon ClAsS")))        # 25

# count the total number of white spaces
print(re.findall(r"\s", "Hello WelCoMe to PytHon ClAsS"))       # [' ', ' ', ' ', ' ']

print(len(re.findall(r"\s", "Hello WelCoMe to PytHon ClAsS")))      # 4





