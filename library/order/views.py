from django.shortcuts import render

def order_page(request):
    if request.method == "GET":
        return render(request, "order/templates.html")
# Create your views here.

