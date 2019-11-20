import string  # importing string to get access for lowercase alphabet symbols

def solve(s):
    streakCounter = 0  # this var ll be a counter of consonant substrings
    tempCounter = 0  # temporary var that allow us to finding consonant substring
    streakList = []  # list ll contain streaks in indexes
    alphDict = dict(zip(string.ascii_lowercase, [num for num in range(1, 27, 1)]))
    for i in list(alphDict):  # using list() for avoid TypeError (dict changed size during iteration)
        if i in list('aeiou'):  # searching for vowels in our dict
            alphDict.pop(i)
        else:
            pass
            
    for sym in s:
        if sym in list(alphDict):  # using list() again to index letters without vowels
            streakCounter += 1
            tempCounter += alphDict[sym]
        else:
            if streakCounter > 0:
                streakList.append(tempCounter)
                tempCounter = 0
                streakCounter = 0
            else:
                pass
            
    return max(streakList)
