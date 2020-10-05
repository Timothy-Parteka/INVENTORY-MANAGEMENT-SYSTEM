from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser, Department, Role

# Register your models here.

class CustomUserAdmin(UserAdmin):

    add_form= CustomUserCreationForm

    form = CustomUserChangeForm

    model= CustomUser

    list_display = ('email', 'id_number', 'first_name', 'last_name', 'department', 'is_staff', 'is_active', 'date_joined')

    list_filter = ('email', 'is_staff', 'is_active')

    fieldsets =(
        (None, {'fields': ('email', 'password', 'id_number', 'first_name', 'last_name', 'department', 'role', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields':('email', 'password1', 'password2', 'is_staff', 'is_active')
        })
    )
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Role)
