def SingleRootWord(rootWord, *otherWords):
    sameWords = []
    for word in otherWords:
        if rootWord.casefold() in word.casefold():
            sameWords.append(word)
    return sameWords


WordsList = ['settlers', 'settlement', 'seller', 'setup', 'seriously']
print(SingleRootWord('able', 'disable', 'enable', 'forecast', 'richable'))
print(*SingleRootWord('settle', *WordsList))
