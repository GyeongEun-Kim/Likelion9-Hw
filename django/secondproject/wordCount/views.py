from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    sentence = request.GET['sentence']

    wordList = sentence.split()

    wordDick = {}

    for word in wordList:
        if word in wordDick:
            wordDict[word] += 1
        else:
            wordDick[word] = 1

return render(request, "result.html", {'fulltext': sentence, 'count':len(wordList), "wordDick":wordDict.items})