

def charCount(word):
    chars = 'йуеыаоэяию'
    count = 0
    for i in list(word):
        if i in chars:
            count = count + 1
    return count

def VinnyPoohFunction(sent, fun):
    words = sent.split()
    curCount = 0
    prevCount = 0
    result = True

    for idx, word in enumerate(words):
        curCount = fun(words[idx])
        prevCount = fun(words[idx-1])
        if curCount != prevCount:
            result = False
            break
    if result:
        print("Парам пам-пам")
    else:
        print("Пам парам")

string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

VinnyPoohFunction(string, charCount)





