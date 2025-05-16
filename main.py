from stats import count_book_words
from stats import sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_location = "books/frankenstein.txt"
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
main()