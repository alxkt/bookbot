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

def sort_on(dict):
  """
  Helper function to sort dictionary by 'number' key.

  Args:
    dict (dict): The dictionary to sort.

  Returns:
    int: The value of the 'number' key.
  """
  return dict["number"]

def sorted_letter_counts(letter_dict):
  """
  Sorts letter counts in a descending order.

  Args:
    letter_dict (dict): Dictionary of letter counts.

  Returns:
    list: Sorted list of letter counts.
  """

  sorted_list = []
  for letter in letter_dict:
    sorted_list.append({"name": letter, "number": letter_dict[letter]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list


def letter_report(sorted_list_of_letters):
  """
  Prints a report of letter counts.

  Args:
    sorted_list_of_letters (list): Sorted list of letter counts.
  """
  for letter in sorted_list_of_letters:
    print(f"{letter['name']}: {letter['number']}")