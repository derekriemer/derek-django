from django.shortcuts import render

def getContext():
    return {
        "MENU_FILE" : "derek_site/menu.htm"
    }

def error404(request):
    return render(request, 'derek_site/404.html', getContext())
