from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    uppercase = request.POST.get('UpperCase', 'default')
    RemSpaces = request.POST.get('RemSpaces', 'default')
    RemPunctuations = request.POST.get('RemPunctuations', 'default')
    ExtraSpaceRem = request.POST.get('ExtraSpaceRem', 'default')
    RemNewline = request.POST.get('RemNewline', 'default')

    fx = ""
    purpose_add = ""

    # RemSpaces
    if RemSpaces == 'on':
        fx = ""
        for char in djtext:
            if char != ' ':
                fx += char
        djtext = fx
        fx = ""

    # RemPunctuations
    if RemPunctuations == 'on':
        fx = ""
        punctuations = '''!"#$%&'()*+,-./:;?@[]\\^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                fx += char
        djtext = fx
        fx = ""

    # uppercase
    if uppercase == 'on':
        for char in djtext:
            fx += char.upper()
        purpose_add += "UpperCase"
        djtext = fx

    # ExtraSpaceRem
    if ExtraSpaceRem == 'on':
        fx = djtext[0]
        for index, char in enumerate(djtext):
            if index > 0:
                if not(djtext[index - 1] == ' ' and djtext[index] == ' '):
                    fx += djtext[index]
    #RemNewline
    if RemNewline == 'on':
        fx = ""
        for char in djtext:
            if char != '\n':
                fx += djtext
                print(char)
        djtext = fx


    yellow = {
        "purpose": purpose_add,
        "analyzed": djtext
    }

    return render(request, 'analyze.html', yellow)
