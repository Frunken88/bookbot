import sys
from stats import words_in_book
from stats import chars_in_book
from stats import present_book
def get_book_text(filepath):
    with open(filepath) as f:
        bok_in = f.read()
        return bok_in

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bok = get_book_text(sys.argv[1])
    kar = chars_in_book(bok)
    word_count = words_in_book(bok)
    pres = present_book(kar)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in pres:
        if char["char"].isalpha() == True:
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()

