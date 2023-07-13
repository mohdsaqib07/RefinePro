from django.http import HttpResponse
from django.shortcuts import render
import string


def about(request):
    return render(request, 'about.html', {"name": "saqib"})


def index(request):
    return render(request, "index.html")


def analyzer(request):
    params = dict()
    if request.method == "POST":
        text = request.POST.get('text', 'default')
        punc = request.POST.get('punc', 'off')
        newline = request.POST.get('newline', 'off')
        space = request.POST.get('space', 'off')
        capfirst = request.POST.get('capfirst', 'off')
        count = request.POST.get('count', 'off')

        if punc == "punc":
            punctuations = string.punctuation
            for p in punctuations:
                text = text.replace(p, "")
            params['purpose'] = 'Remove Punctuation'
        if newline == "newline":
            text = text.replace(r'\n', "")
            params['purpose'] = 'Remove Newline'
        if space == "space":
            temp = text
            text = ""
            for ind, char in enumerate(temp):
                if ind < (len(temp) - 1):
                    if not (temp[ind] == " " and temp[ind + 1] == " "):
                        text += char
            text += temp[len(temp) - 1]
            text = text.rstrip()
            text = text.lstrip()
            params['purpose'] = 'Remove Whitespaces'
        if capfirst == "capfirst":
            text = text.capitalize()
            params['purpose'] = 'Capitalize the first charcater of the string'
        if count == "count":
            text = len(text)
            params['purpose'] = 'Counting number of the chracters'
        if punc == "off" and newline == "off" and space == "off" and capfirst == "off" and count == "off":
            return HttpResponse('Error')
        params['analyzetext'] = text
        print(text)
        # return HttpResponse(f'<h1>Analyzer Purpose : {params["purpose"]}</h1><p>{params["analyzetext"]}</p')
        return render(request, 'analyzer.html', params)
