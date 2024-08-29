def main():
  path_to_book = "books/frankenstein.txt"
  text = get_book_text(path_to_book)
  letters = letter_frequency(text)
  sorted_letters = sorted_letter_counts(letters)
  letter_report(sorted_letters)
  return

def get_book_text(path):
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
  return file_contents

def string_to_words(string):
  words = string.split()
  return words

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

def sort_on(dict):
  return dict["number"]

def sorted_letter_counts(letter_dict):
  sorted_list = []
  for letter in letter_dict:
    sorted_list.append({"name": letter, "number": letter_dict[letter]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list


def letter_report(sorted_list_of_letters):
    for letter in sorted_list_of_letters:
      print(f"{letter['name']} appears {letter['number']} times")

main()