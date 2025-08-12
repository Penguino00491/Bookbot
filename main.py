from stats import word_count, character_count, sorted_char_counts
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_filepath = sys.argv[1]

def get_book_text(book_directory: str) -> str: 
    with open(book_directory) as file:
        book_text = file.read()
    return book_text

def main():
    book_string = get_book_text(book_filepath)
    return book_string

book_as_text = main()

print("============ BOOKBOT ============")
print(f"Analyzing book: found at {book_filepath}...")
print("----------- Word Count ----------")
word_count_result = word_count(book_as_text)
print(f"Found {word_count_result} total words")
print("--------- Character Count -------")
char_count_result = character_count(book_as_text)
sorted_char_counts_result = sorted_char_counts(char_count_result)
for dictionary in sorted_char_counts_result:
    if dictionary["char"].isalpha():
        print(f"{dictionary["char"]}: {dictionary["num"]}")
print("============= END ===============")