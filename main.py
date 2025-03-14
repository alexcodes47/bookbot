# import os
# print(os.getcwd())

import sys
from stats import count_words, count_characters, get_sorted_char_counts

if len(sys.argv) != 2:
    # This means the user didn't provide exactly one argument
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Store the book path from command line arguments
book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main(): 
    file_contents = get_book_text(book_path)
    # print(file_contents)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_counts = get_sorted_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_counts:
        if entry['char'].isalpha():  # Only process alphabetical characters
            print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")
    # print(sorted_counts)

if __name__ == "__main__":
    main()