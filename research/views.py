from django.shortcuts import render, redirect
from . import func
from . models import UserEmail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

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
            user_id_base_64 = urlsafe_base64_encode(str(useremail.id).encode('utf-8'))
            print(code)
            return redirect(f"/p/email-confirmation-{user_id_base_64}")
        except:
            message = "Cet email exist déjà"
            context["message"] = message

    return render(request, "research/alert.html", context)

def confirm_email(request, base64):
    context = {}
    id_base64 = base64.split("-")[2]
    try:
        user = UserEmail.objects.get(pk=urlsafe_base64_decode(id_base64))
    except:
        return handler404(request, exception=404)
    else:
        if request.method=="POST":
            code = request.POST.get("code")
            if user.code == code:
                user.valid=True
                user.save()
                context['success'] = "Mail validé !"
            else:
                message = 'Code incorrect'
                context['message'] = message
        context['username'] = user.name
    return render(request, "research/confirm_email.html", context)

def handler404(request, exception):
    return render(request, "research/errors/404.html", status=404)

def handler500(request):
    return render(request, "research/errors/500.html", status=500)
