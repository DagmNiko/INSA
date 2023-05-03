from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_superuser')


admin.site.register(Account, AccountAdmin)