from django.db import models
from django.contrib import admin

class UserEmail(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    valid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

class UserEmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'code', 'valid']