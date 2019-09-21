from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return render(request,'index1.html')

      
def analyze(request):
    ##get the text
    param=request.POST.get('text','default')

    ###get the on off value
    removepunc=request.POST.get('removepunc','off')
    capital=request.POST.get('capitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    
    if removepunc=="on":
        punctuations=" !()[]{ }:;,<>./?&@#$%@-~"
        analyzed=''
        for char in param:
            if char not in  punctuations:
                analyzed= analyzed+ char
        parameter={'analyze':'Your Analyze','analyze_te':analyzed}
        param=analyzed

    if(capital=='on'):
        analyzed=''
        for char in param:
            analyzed= analyzed+ char.upper()
        parameter={'analyze':'Capitalize Word:','analyze_te':analyzed}
        param=analyzed
    
    if (newlineremover=='on'):
        analyzed=''
        for char in param:
            if char !="\n":
                analyzed= analyzed+ char
        parameter={'analyze':'New line remover:','analyze_te':analyzed}
        param=analyzed

    if (spaceremover=='on'):
        analyzed=''
        for index,char in enumerate(param):
            if not(param[index]==" " and param[index+1]==" "):
                analyzed=analyzed+char
        parameter={'analyze':'Space remover:','analyze_te':analyzed}
        param=analyzed
    
    if (removepunc !='on' and capital!='on' and newlineremover!='on' and spaceremover!='on' ):
        return HttpResponse("There is something seriously wrong thing going on !!!  HUH !!!!!")
        
    return render(request,'analyze.html',parameter) 
    
        


        

    