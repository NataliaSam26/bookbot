from stats import get_word_count, get_chars_count, get_sorted_list_of_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # exit the program with a status code of 1
    return get_book_text(sys.argv[1]), sys.argv[1]

book_text, path = main()

total_words = get_word_count(book_text)
chars_count = get_chars_count(book_text)
sorted_list = get_sorted_list_of_dicts(chars_count)

alphabetical_items = [item for item in sorted_list if item['char'].isalpha()]
result = ""
for item in alphabetical_items:
    result += f"{item['char']}: {item['num']}\n"


print(f"============ BOOKBOT ============\n"
      f"Analyzing book found at {path}...\n"
      f"----------- Word Count ----------\n"
      f"Found {total_words} total words\n"
      f"--------- Character Count -------\n"
      f"{result}"
      f"============= END ==============="
      )



