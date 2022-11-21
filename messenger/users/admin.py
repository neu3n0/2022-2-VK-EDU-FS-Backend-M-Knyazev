from django.contrib import admin
from .models import User, Contactbook

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'age', 'mobile', 'description')
    model = User


@admin.register(Contactbook)
class ContactbookAdmin(admin.ModelAdmin):
    filter_horizontal = ('contacts',)
    model = Contactbook