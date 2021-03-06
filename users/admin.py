from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, ConnectionType, ConnectionSubtype, Connections


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('bio', 'photo',)}),
    )
    model = CustomUser
    list_display = ['email', 'username', 'bio']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ConnectionType)
admin.site.register(ConnectionSubtype)
admin.site.register(Connections)
