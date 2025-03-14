import sys
from stats import count_words, count_characters, sort_dictionaries


def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(filepath, words_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char, count in char_counts:
        print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    num_chars = count_characters(book_text)
    sorted_dictionaries = sort_dictionaries(num_chars)

    # Extract list of tuples [(char, count), ...]
    char_counts = [(item["char"], item["count"]) for item in sorted_dictionaries]
    
    print_report(file_path, num_words, char_counts)


main()
