# from django.shortcuts import render

# # Create your views here.


# from django.http import HttpResponse
# # Create your views here.

# def index(request):
#     return HttpResponse("Index blog")


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"blog/index.html")

