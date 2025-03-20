def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def numWords(bookText):
    wordsList = bookText.split()
    return len(wordsList)


def main():
    text = get_book_text("./books/frankenstein.txt")
    numOfWords = numWords(text)
    print(f"{numOfWords} words found in the document")






main()