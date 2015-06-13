from django.shortcuts import render
from django.http import Http404

#helper functions.
def getContext():
    return {
        "MENU_FILE" : "personal/menu.htm"
    }

#views
def index(request):
    context=getContext()
    return render(request, 'personal/index.htm', context)

def bio(request):
    context=getContext()
    return render(request, 'personal/bio.htm', context)
