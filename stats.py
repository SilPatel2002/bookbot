def numWords(bookText):
    wordsList = bookText.split()
    return len(wordsList)


def getCharNum(bookText):
    charDict ={}
    wordsList = bookText.split()
    for word in wordsList:
        for char in word.lower():
            if char in charDict:
                charDict[char] += 1
            
            else:
                charDict[char] = 1

    return charDict