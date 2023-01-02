from django.shortcuts import render,HttpResponse

# Create your views here.
def product_view(request):
    return HttpResponse("<h2>My first Django Project</h2>")
    
