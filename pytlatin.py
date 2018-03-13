# This code was written on a basis of Codecademy guide [link](https://www.codecademy.com/courses/learn-python/lessons/pyglatin)
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print 'THIS IS THE BOMB'
  word = original.lower()
  first = word[0]
  word_2 = word[1:]
else:
  print 'empty'
new_word = word_2 + first + pyg
print new_word
