
import sys
from stats import letter_frequency, get_num_words, sorted_letter_counts, letter_report

def main():
  """
  Main function to analyze a book text file and print word and letter counts.
  """
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    return

  path_to_book = sys.argv[1]
  try:
    text = get_book_text(path_to_book)
  except FileNotFoundError:
    print(f"Error: File not found at {path_to_book}")
    return

  letters = letter_frequency(text)
  sorted_letters = sorted_letter_counts(letters)
  num_words = get_num_words(text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_book}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  letter_report(sorted_letters)
  return

def get_book_text(path):
  """
  Reads the content of a book file.

  Args:
    path (str): The path to the book file.

  Returns:
    str: The content of the book file.
  """
  with open(path) as f:
    file_contents = f.read()
  return file_contents

if __name__ == "__main__":
  main()