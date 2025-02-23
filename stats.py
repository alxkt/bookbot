def get_num_words(string):
  return len(string.split())

def letter_frequency(string):
  letters = {} 
  lowercase_string = string.lower()
  for letter in lowercase_string:
    if letter.isalpha():
      if letter in letters:
        letters[letter] += 1
      else:
        letters[letter] = 1
  return letters