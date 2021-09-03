from django.shortcuts import render
from .models import *
from collections import Counter
import json
from django.http import JsonResponse
from datetime import datetime
# Create your views here.

def home(request):
    allKeywords = Keyword.objects.all()
    keyWord = []
    words = []
    for i in allKeywords:
        w = i.keyword
        keyWord.append(w)

        while len(w) > 0:
            if ' ' in w:
                index = w.index(' ')
                words.append(w[:index])
                w = w[index+1:]
            else:
                words.append(w)
                w = ''

    counter = Counter(words)
    myword = []
    for k,v in counter.items():
        obj = {}
        obj[k] = v
        myword.append(obj)
    

    counter2 = Counter(keyWord)
    myKeyWord = []
    for k,v in counter2.items():
        obj = {}
        obj[k] = v
        myKeyWord.append(obj)


    return render(request, 'home.html', {
        'allKeywords': allKeywords,
        'specificWordsSet': set(words),
        'myword': myword,
        'myKeyWord': myKeyWord,
        'allUsers': User.objects.all()
    })


def getAllResult(request):
    result = Keyword.objects.all().order_by('-date')
    allResult = []
    for i in result:
        obj = {}
        w = i.keyword
        obj['fullKeyword'] = w
        wl = []
        while len(w) > 0:
            if ' ' in w:
                index = w.index(' ')
                wl.append(w[:index])
                w = w[index+1:]
            else:
                wl.append(w)
                w = ''
        obj['specificKeyword'] = wl
        obj['user'] = i.user.user
        obj['date'] = i.date.strftime('%Y-%m-%d')
        allResult.append(obj)

    # k = Keyword.objects.get(id=3)
    # k.date = '2021-07-30 20:11:24.084774'
    # k.save()
    # print(k.date)
    return JsonResponse({'result': allResult})