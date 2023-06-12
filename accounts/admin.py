from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Belt, Category, Task, PatientTest, FormQuestion, Progress, AssignedTask


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('email','first_name', 'last_name', 'program')
    list_filter = ('email','first_name', 'last_name', 'program')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name','program')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
        'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}))


    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('first_name','last_name', 'email', 'password1', 'password2', 'program', 'is_staff', 'is_active',)}
        ),
    )
    
    search_fields = ('email','first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('task', 'user', 'belt', 'category')
    list_filter = ('user', 'belt', 'category')

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(Task)
admin.site.register(PatientTest)
admin.site.register(FormQuestion)
admin.site.register(AssignedTask)


# Need users page
# Need patient test creation
