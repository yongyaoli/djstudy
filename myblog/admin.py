from django.contrib import admin
from .models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'passwd', 'age', 'phone', 'add_time')


admin.site.register(Users, UsersAdmin)