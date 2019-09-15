# I HAVE CREATED THIS FILE #
from django.http import HttpResponse
from django.shortcuts import render



#code for pipeline
def index(request):
  
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')
    
    #checkbox values
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')





    #check which checkbox is on
    if removepunc=="on":
        punctuation= '''!()=[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed="" 
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed + char
        p={'purpose':'Remove punctuation', 'analyzed_text':analyzed}
        djtext=analyzed
        
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        p={'purpose':'changed to upper case', 'analyzed_text':analyzed}
        djtext=analyzed
        
    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed + char
        p={'purpose':'removed new lines', 'analyzed_text':analyzed}
        djtext=analyzed
        
    if (extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed + char
        p={'purpose':'extra space remover', 'analyzed_text':analyzed}
        djtext=analyzed
      
    
    if (charcount=="on"):
        analyzed=""
        count=0
        for char in djtext:
            count=count+1
            analyzed = analyzed + char  
        p={'purpose':'charcount', 'analyzed_text':analyzed, 'n':count}
        djtext=analyzed
       
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Error please select any operation")
    
    return render(request, 'analyze.html', p)

