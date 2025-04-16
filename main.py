from stats import get_num_words, get_char_count, create_list
from sys import argv

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    text = get_book_text(argv[1])
    word_count = get_num_words(text)
    sorted_char_list = create_list(get_char_count(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()