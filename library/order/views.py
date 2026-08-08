from django.shortcuts import render

# Create your views here.

def order_page(request):
    if request.method == "GET":
        return render(request, "order/templates.html")
# Create your views here.

