from stats import get_book_text, word_count, count_characters, sorted_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book_path =sys.argv[1] 
    print("============ BOOKBOT ============")
    # print(get_book_text("books/frankenstein.txt"))
    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(book_path)
    w_count = word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    character_count = count_characters(book_text)
    # print(character_count)
    print("--------- Character Count -------")
    sorted_chars = sorted_dict(character_count)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")



main()

