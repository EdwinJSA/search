from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'FindMe'})

def imageSearch(request):
    return render(request, 'imageSearch.html', {'title': 'Image Search'})

def advanceSearch(request):
    return render(request, 'advanceSearch.html', {'title': 'Advanced Search'})

def searching(request):
    search_query = request.GET['q']
    query = f'https://www.google.com/search?q={search_query}&btnI'
    return redirect(query)

def simplesearch(request):
    search_query = request.GET['q']
    query = f'https://www.google.com/search?q={search_query}'
    return redirect(query)