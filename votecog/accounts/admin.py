from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
# Register your models here.
from .models import Person


class CandidateForm(admin.ModelAdmin):
    list_display = ('name','email','year','bio')
    search_fields = ('email', 'name')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Person,CandidateForm)

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_voter', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)