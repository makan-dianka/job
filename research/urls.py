from django.urls import path
from . import views

app_name="research"

urlpatterns = [
    path('', views.index, name="index"),
    path('alert', views.alert, name="alert"),
    path('p/<str:base64>', views.confirm_email, name="confirm_email"),
]