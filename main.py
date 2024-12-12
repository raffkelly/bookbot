def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    print(f"--- Begin report of {book_path} ---")
    print(f"Total word count: {num_words}")
    sorted_characters = sorted_character_count(character_count(book_text))
    print("Character count:")
    for char in sorted_characters:
        if char["char"].isalpha():
            print(f"{char["char"]} is used {char["num"]} times.")


def get_book_text(book_path):
    with open(book_path) as f:
       return f.read()


def word_count(book):
    words = book.split()
    return len(words)


def character_count(book):
    char_count = {}
    book = book.lower()
    for character in book:
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1
    return char_count


def sort_on(dict):
    return dict["num"]    
     

def sorted_character_count(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()