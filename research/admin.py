from django.contrib import admin
from . models import (
    UserEmail,
    UserEmailAdmin
)

admin.site.register(UserEmail, UserEmailAdmin)
