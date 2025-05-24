import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1);

    path = sys.argv[1];


    book_text = get_book_text(path);
    num_words = get_num_words(book_text);
    num_characters = get_num_characters(book_text);
    sorted_num_characters = sort_num_characters(num_characters);

    print("============ BOOKBOT ============");
    print("Analyzing book found at {path}");
    print("----------- Word Count ----------");
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for char in num_characters:
        if char.isalpha():
            print(f"{char}: {num_characters[char]}")

    print("============= END ===============");
    


main()
