# file by me - rohit
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req, 'index.html',)
def about(request):
    return render(request, 'about.html', )
def contact(request):
    return render(request, 'contact.html', )

def analyze(request):
    djtext = request.POST.get('textarea', 'default')
    rempunc = request.POST.get('rempunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    char_counter = request.POST.get('char_counter', 'off')

    if rempunc == "on":
        punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        for char in djtext :
            if char not in punctuations : 
                analyzed = analyzed + char

        params = {
            'purpose' : 'Removed Punctuations',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()

        params = {
            'purpose' : 'Changed to Uppercase',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext :
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {
            'purpose' : 'Removed the new line',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if extra_space_remover == "on":
        analyzed = ""
        for index, char in enumerate(djtext) :
            if not ( char == " " and index + 1 < len(djtext) and djtext[index + 1] == ' ' ):
                analyzed = analyzed + char 

        params = {
            'purpose' : 'Removed the extra spaces',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if char_counter == "on":
        analyzed = len(djtext)
        params = {
            'purpose' : 'Total Characters',
            'analyzed_text' : analyzed
        }
        djtext = analyzed

    if(rempunc != "on" and fullcaps != "on" and newlineremover != "on" and extra_space_remover != "on" and char_counter != "on" ) :
        return render(request, 'error.html', )

    return render(request, 'analyze.html', params)