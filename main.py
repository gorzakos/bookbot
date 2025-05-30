from stats import count_words, count_characters
import sys

if not len(sys.argv) == 2:
    exit_message = "Usage: python3 main.py <path_to_book>"
    print(exit_message)
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath)as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    sorted_character_counts = count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_character_counts:
        c = d["char"]
        if c.isalpha():
            n = d["num"]
            print(f"{c}: {n}")
    print("============= END ===============")


main()
