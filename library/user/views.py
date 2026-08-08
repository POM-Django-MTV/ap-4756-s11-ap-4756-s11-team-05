from django.shortcuts import render

def user_page(request):
    if request.method == "GET":
        return render(request, "user/templates.html")
# Create your views here.

