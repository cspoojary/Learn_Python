# Count frequency of each character in a string
'''
str = "chaithanya"
freq = {}
for ch in str:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq)
'''

# Find first non-repeating character in a string
'''
str = "caaidffcai"
freq = {}

for ch in str:
    freq[ch] = freq.get(ch,0)+1

for ch in str:
    if freq[ch] == 1:
        print(ch)
        break
'''

# Check whether two strings are anagrams
'''
str1 = "silent"
str2 = "listen"
if sorted(str1) == sorted(str2):
    print("Given two strings are anagaram")
else:
    print("The given string is not anagram")
'''


# Remove all special characters from a string
'''
import re

str = "Hello@World! 123#Python$"
clean =re.sub(r'[^A-Za-z0-9]',' ',str)
print(clean)
'''

# Find all duplicate characters in a string
'''
str = "chaithanya"
freq = {}
dup = []
for ch in str:
    freq[ch] = freq.get(ch,0)+1

    if freq[ch] == 2:
        dup.append(ch)
print(dup)
'''

# Reverse words in a sentence
'''
sen = "I love Python Programming Language"
lst = sen.split()
for word in range(len(lst)):
    lst[word] = lst[word][::-1]
print(lst)
'''

# Check if a string contains only digits
'''
str = "12345"
flag = True

for ch in str:
    if ch < '0' or ch > '9' :
        flag=False
        break

if flag:
    print("Only digit")
else:
    print("Not only digit")
'''

# Find the longest word in a sentence
'''
sen = "I love Python Programming Language"
lst = sen.split()
lenthiest = ""

for i in lst:
    for j in lst:
        if len(i) > len(j):
            lenthiest = i
        elif len(j) > len(i):
            lenthiest = j
print(lenthiest)
'''

# Count number of words in a string
'''
str = "Chaithanya"
count = 0
for ch in str:
    count = count+1
print(count)
'''

# Convert string to title case without using built-in methods
'''
def to_title_case(s):
    result = ""
    new_word = True

    for ch in s:
        if ch == ' ':
            result += ch
            new_word = True
        else:
            if new_word:
                # convert lowercase to uppercase
                if 'a' <= ch <= 'z':
                    result += chr(ord(ch) - 32)
                else:
                    result += ch
                new_word = False
            else:
                # convert uppercase to lowercase
                if 'A' <= ch <= 'Z':
                    result += chr(ord(ch) + 32)
                else:
                    result += ch

    return result


print(to_title_case("Hello worlD fRom python"))

'''

