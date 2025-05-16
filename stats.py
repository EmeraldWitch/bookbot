def count_book_words(book):
    num_words = 0
    for string in book.split():
        num_words += 1
    return num_words

def count_characters(book):
    book_lower = book.lower()
    character_dictionary = {}
    for string in book_lower.split():
        for character in string:
            if character not in character_dictionary:
                character_dictionary[character] = 1
            else: character_dictionary[character] += 1
    return character_dictionary

def sorted_dictionary(book):
    char_dict = []
    def sort_on(dict):
        return dict["num"]
    for key, value in count_characters(book).items():
        char_dict.append({"char": key, "num": value})
    char_dict.sort(reverse=True, key=sort_on)

    return char_dict