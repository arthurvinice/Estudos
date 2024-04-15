# A code challenge answer for Codrebyte.com
# Have the function LongestWord(sen)
# take the sen parameter being passed and return the longest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

import string
def LongestWord(sen):
  table = str.maketrans('', '', string.punctuation)
  words = sen.split()
  longest = ''
  for word in words:
    word_no_punctuation = word.translate(table)
    if len(word_no_punctuation) > len(longest):
        longest = word_no_punctuation
          
  return longest

# keep this function call here 
print(LongestWord(input()))
