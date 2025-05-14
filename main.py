import sys
from stats import get_characters_count, get_num_words, get_sorted_list_from_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        return file

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    characters_count = get_characters_count(text)
    sorted_list = get_sorted_list_from_dictionary(characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")


main()
