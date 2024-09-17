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

###############################################################################

# meta characters
# '+' -> matches 1 or more times

# match any digit from 0 to 9 as long as it matches
print(re.findall(r"[0-9]+", "The cost of 10 gram gold is 72345"))   # ['10', '72345']

# match one or more occurrences of character n between a and b
print(re.findall(r"an+b", "annnbanbnnannnnnnnnnbabnnnnnannnnnnnnnnbannb"))      # ['annnb', 'anb', 'annnnnnnnnb', 'annnnnnnnnnb', 'annb']

# match all lowercase characters as long as it matches
print(re.findall(r"[a-z]+", "Hello WelCoMe to PytHon ClAsS"))       # ['ello', 'el', 'o', 'e', 'to', 'yt', 'on', 'l', 's']
print(re.findall(r"[A-Za-z]+", "Hello WelCoMe to PytHon ClAsS"))        # ['Hello', 'WelCoMe', 'to', 'PytHon', 'ClAsS']

# find the sum of numbers in the string
st = "1s65kl4sf678jsl345knkl34jk1111"
# o/p1 = 1 + 6 + 5 + 4 + 6 + 7 + 8 + 3 + 4 + 5 + 3 + 4 + 1 + 1 + 1 + 1
# o/p2 = 1 + 65 + 4 + 678 + 345 + 34 + 1111

nums1 = re.findall(r"[0-9]", st)
nums2 = re.findall(r"[0-9]+", st)
# print(nums1, nums2)
s1, s2 = 0, 0
for num in nums1:
    s1 += int(num)

for num in nums2:
    s2 += int(num)

print(s1)   # 60
print(s2)   # 2238

# Meta character '?'

# July or Jul
print(re.findall(r"July?", "20 July 2020 20 Jul 2024"))     # ['July', 'Jul']

# Negation '^'
print(re.findall(r"[^0-9]", "The cost of 10 gram gold is 72345"))

print(re.findall(r"[^a-z]", "The cost of 10 gram gold is 72345"))

# count the number of special characters

print(re.findall(r"[^A-Za-z0-9]", "as#$jkf987&*%*_ +="))

####################################################################################

# word boundary (\b)

print(re.findall(r"day", "what a beautiful day today is, I had a daydream"))    # ['day', 'day', 'day']

print(re.findall(r"\bday", "what a beautiful day today is, I had a daydream"))  # ['day', 'day']

print(re.findall(r"day\b", "what a beautiful day today is, I had a daydream"))  # ['day', 'day']

print(re.findall(r"\bday\b", "what a beautiful day today is, I had a daydream"))    # ['day']


# match the words starting with 'p'

sentence = 'prakriti is learning python from pyspiders'
print(re.findall(r"\bp[a-zA-Z]+", sentence))    # ['prakriti', 'python', 'pyspiders']

# match the words starting with P or p
sentence = 'Prakriti is learning python from PySpiders'
print(re.findall(r"\b[pP][a-zA-Z]+", sentence))     # ['Prakriti', 'python', 'PySpiders']

print(re.findall(r"(?:p|P)[a-zA-Z]+", sentence))    # ['Prakriti', 'python', 'PySpiders']

# expression to match names ending with a or i

names = "hari krishna kavya abhishek ram nandini"

print(re.findall(r"[a-zA-Z]+[ai]\b", names))    # ['hari', 'krishna', 'kavya', 'nandini']

# expression to match the words starting with capital letter
sentence = 'Prakriti is learning python from PySpiders sPoon'
print(re.findall(r"\b[A-Z][A-Za-z]+", sentence))    # ['Prakriti', 'PySpiders']

# expression to match words with lowercase characters only
print(re.findall(r"\b[a-z]+\b", sentence))      # ['is', 'learning', 'python', 'from']

# expression to match words starting with vowel only
words = "abhi Aradhya Vivek rahul uday"
print(re.findall(r"\b[aeiouAEIOU][a-zA-Z]+", words))    # ['abhi', 'Aradhya', 'uday']

# count the number of spaces in sample.log
sample_log_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_M80\10_File_Handling\sample.log"

with open(sample_log_path) as file:
    white_spaces = 0
    for line in file:
        white_spaces += len(re.findall(r"\s", line))
    print(white_spaces)

# count the number of capital letter words in sample.log
with open(sample_log_path) as file:
    count = 0
    for line in file:
        count += len(re.findall(r"\b[A-Z]+\b", line))
    print(count)


# count the number of capital letters in sample.log -> r"[A-Z]"
# count the number of 'INFO', 'TRACE', 'WARNING', 'EVENT' messages
# {'INFO': 147, 'TRACE': 119, 'WARNING': 4, 'EVENT': 13}

with open(sample_log_path) as file:
    data = file.read()
    print(len(re.findall(r"EVENT", data)))


# count the number of words in sample.log

with open(sample_log_path) as file:
    count = 0
    for line in file:
        count += len(re.findall(r"\b[A-Za-z0-9]+", line))
    print(count)

###############################################################################

# match all the digits
sentence = "The cost of 1 kilogram of mango is 90 and that of orange is 67"
print(re.findall(r"\d", sentence))      # ['1', '9', '0', '6', '7']

# match the numbers
print(re.findall(r"\d+", sentence))     # ['1', '90', '67']

#  match exactly 2 digit number

nums = '64 358 3 9875 45 76'
print(re.findall(r"\b\d{2}\b", nums))       # ['64', '45', '76']

# match 2 or 3 digit number
print(re.findall(r"\b\d{2,3}\b", nums))     # ['64', '358', '45', '76']

###############################################################################

# match phone number pattern - 9876543210 7889654321
print(re.findall(r"\b[6-9][0-9]{9}\b", "9876543210 1234567890 2345678901 6789012345987"))

# match ip address -> 197.234.4.34
print(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "198.23.333.8 1234.98.98.234 19.86.8.2 198.48.89989.8"))

# match university numbers - 1PI13CS087     -> region code (1st number) has to be either 1, 2, 3 or 4

expression = r"\b[1-4][A-Z]{2}\d{2}[A-Z]{2}\d{1,3}\b"
st = "1PI13EC036 1PI13CS736"

print(re.findall(expression, st))

# match pan card number -> COIPB0809E
st = "COIPB0809E ABCDE09888Y  COIPB8789"
print(re.findall(r"\b[A-Z]{5}\d{4}[A-Z]", st))  # ['COIPB0809E']

# expression to match 3 letter word in a given sentence
sentence = "Hai Eve, how are you doing"
print(re.findall(r"\b[a-zA-Z]{3}\b", sentence))

# meta character '*' -> match 0 or more expressions

# match words starting with he
sentence = 'if he does not help the poor, he will go to hell'
print(re.findall(r"\bhe[A-Za-z]*", sentence))   # ['he', 'help', 'he', 'hell']

# escaping a meta character
# count the number of ?
sentence = "hello there? how are you? how is life? what are you doing?"
print(len(re.findall(r"\?", sentence)))     # 4

# count the number of +
# count the number of *

# match puython or java
print(re.findall(r"(python|java)", "python and java are programming languages"))    # ['python', 'java']

# match the words starting with he or se
sentence = "she sells sea shells in the seashore, he helps the community and he is the hero"
print(re.findall(r"\b(?:he|se)[a-zA-Z]*\b", sentence))      # ['he', 'sells', 'sea', 'hells', 'he', 'seashore', 'he', 'helps', 'he', 'he', 'he', 'hero']

# expression to match email

emails = """
test.user@gmail.com
test.user2@gmail.com
test2.user@gmail.com
testuser@company.in
testuser2@company.com
"""

"""
com, in, edu, gov, org
(?:com|in|edu|org|gov)

gmail, company
[a-z]+

tester, test2, 2tester
[a-z0-9]+

\.

"""

email_pattern = r"[a-z0-9]+.?[a-z0-9]*@[a-z]+.?(?:com|in|gov|org|edu)"
print(re.findall(email_pattern, emails))




