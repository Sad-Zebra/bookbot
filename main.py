def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():
    from stats import word_count
    book = get_book_text("books/frankenstein.txt")
    num_of_words = word_count(book)
    print(num_of_words, "words found in the document")

main()
    

    