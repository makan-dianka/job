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
