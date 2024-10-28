def CountCalls():
    global calls
    calls += 1
    return calls


def StringInfo(Mystring):
    CountCalls()
    StringInfo = (len(Mystring), Mystring.upper(), Mystring.lower())
    return StringInfo


def IsContains(SearchString, ListForSearch):
    CountCalls()
    for element in ListForSearch:
        if element.casefold() == SearchString.casefold():
            return True
    return False


calls = 0
print(StringInfo("BiG WoRlD"))
print(StringInfo("I'm REALLY happy!"))
print(IsContains("Mommy", ['daddy', 'MoMmy', 'grandMA']))
print(IsContains("-million", ['Million', 'BILLION', 'TriLLioN']))
print(calls)
