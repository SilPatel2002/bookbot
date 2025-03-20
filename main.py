from stats import numWords, getCharNum



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    text = get_book_text("./books/frankenstein.txt")
    numOfWords = numWords(text)
    dictionary = getCharNum(text)
    print(f"{numOfWords} words found in the document")

    for key in dictionary:
        print(f"'{key}': {dictionary[key]}")
        print()






main()