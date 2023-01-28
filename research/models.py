from django.db import models
from django.contrib import admin

class UserPreference(models.Model):
    REGIONS=(
        ('paris', 'Paris'),
        ('herault', 'Montpellier'),
        ('toulouse', 'Toulouse'),
        ('autre', 'Autre'),
    )
    LANG=(
        ('python', 'Python'),
        ('php', 'Php'),
        ('java', 'Java'),
        ('autre', 'Autre')
    )
    region = models.CharField(max_length=100, choices=REGIONS)
    lang = models.CharField(max_length=100, choices=LANG)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.lang} - {self.region}"


class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ['region', 'lang', 'create_at']

class UserEmail(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    valid = models.BooleanField(default=False)
    user_preference = models.ForeignKey(UserPreference, on_delete=models.DO_NOTHING, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def preference(self):
        return f"{self.user_preference.lang} - {self.user_preference.region}"

class UserEmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'code', 'valid', 'preference', 'create_at']
