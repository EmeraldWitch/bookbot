from stats import count_book_words
from stats import sorted_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_location = ""
    if len(sys.argv) > 1:
        book_location = sys.argv[1]
    if book_location != "":
        book = get_book_text(book_location)
        word_count = count_book_words(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_dictionary(book):
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()