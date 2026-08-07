from django.shortcuts import render

def book_page(request):
    if request.method == "GET":
        return render(request, "book/templates.html")
# Create your views here.

