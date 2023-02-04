from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    context = {}
    if request.method=="POST":
        mail = request.POST.get("mail")
        obj = request.POST.get("obj")
        text = request.POST.get("text")
        info = {
            "text" : text,
            "username" : "Toto"
        }
        template_email = render_to_string('emailing/email.html', info)
        email = EmailMessage(obj, template_email, settings.EMAIL_HOST_USER, [mail])
        email.content_subtype = "html"
        # email.attach_file(f"{settings.MEDIA_ROOT}/cv_makan.pdf")
        email.fail_silently = False
        try:
            email.send()
            context["success"] = "Message envoyé."
        except:
            context["error"] = "Message non envoyé. Réessayer"
    return render(request, "emailing/index.html", context)
