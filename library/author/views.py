from django.shortcuts import render

def author_page(request):
    if request.method == "GET":
        return render(request, "author/templates.html")
# Create your views here.

