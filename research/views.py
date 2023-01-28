from django.shortcuts import render
from . import func
from . models import UserEmail

# Create your views here.
def index(request):
    if request.method=="POST":
        keyword = request.POST.get("keyword")
        emploi = func.data(keyword)
        return render(request, 'research/result.html', {"data" : emploi})

    return render(request, 'research/index.html')

def alert(request):
    context = {}
    if request.method=="POST":
        email = request.POST.get("email")
        name = request.POST.get('name')
        code = func.code(8)
        useremail = UserEmail(email=email, name=name, code=code, valid=False)
        try:
            useremail.save()
        except:
            message = "Cet email exist déjà"
            context["message"] = message

    return render(request, "research/alert.html", context)

def handler404(request, exception):
    return render(request, "research/errors/404.html", status=404)

def handler500(request):
    return render(request, "research/errors/500.html", status=500)
