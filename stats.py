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

def sortDictionaryHelper(dict):
    return dict["num"]

def sortDictionary(dict):

    dictList =[]

    for key in dict:
        tempDict = {"letter" : key, "num" : dict[key]}
        dictList.append(tempDict)

    dictList.sort(reverse = True, key = sortDictionaryHelper)

    return dictList