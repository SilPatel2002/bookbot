from stats import numWords, getCharNum, sortDictionary, sortDictionaryHelper
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    filepath = sys.argv[1]
    text = get_book_text(filepath)
    numOfWords = numWords(text)
    dictionary = getCharNum(text)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {numOfWords} total words")
    print ("--------- Character Count -------")

    sortedDictionaryList = sortDictionary(dictionary)

    for dict in sortedDictionaryList:
        if dict['letter'].isalpha():
            print(f"{dict['letter']}: {dict['num']}")



    print("============= END ===============")






main()