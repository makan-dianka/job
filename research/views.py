from django.shortcuts import render
from django.http import JsonResponse
from . import func

# Create your views here.
def index(request):
    if request.method=="POST":
        keyword = request.POST.get("keyword")
        emploi = func.data(keyword)
        return render(request, 'research/result.html', {"data" : emploi})

    return render(request, 'research/index.html')

def alert(request):
    return render(request, "research/alert.html")

def handler404(request, exception):
    return render(request, "research/errors/404.html", status=404)

def handler500(request):
    return render(request, "research/errors/500.html", status=500)
