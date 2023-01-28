from django.contrib import admin
from . models import (
    UserEmail,
    UserEmailAdmin,
    UserPreference,
    UserPreferenceAdmin
)

admin.site.register(UserEmail, UserEmailAdmin)
admin.site.register(UserPreference, UserPreferenceAdmin)
