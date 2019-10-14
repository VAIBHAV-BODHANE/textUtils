from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    textBox = request.POST.get('text', 'default')
    print(textBox)
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in textBox:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        textBox = analyzed

    if uppercase == 'on':
        analyzed = ''
        for char in textBox:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        textBox = analyzed

    if lineremover == 'on':
        analyzed = ''
        for char in textBox:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        textBox = analyzed

    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(textBox):
            if not (textBox[index] == " " and textBox[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        textBox = analyzed

    if charcounter == 'on':
        analyzed = ""
        count = 0
        for char in textBox:
            if char != " " and char !="\n" and char != "\r":
                count += 1
        analyzed = analyzed + str(count)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if ( removepunc != "on" and uppercase != "on" and lineremover != "on" and spaceremover != "on" and charcounter != "on"):
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)


