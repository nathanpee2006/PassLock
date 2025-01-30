from django.contrib import admin

from .models import User, Login, Card, PIN, SecureNote


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "salt")

class LoginAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "username", "password", "password_nonce", "password_tag") 

class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "number", "cvv") 

class PINAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "code", "code_nonce", "code_tag") 

class SecureNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "notes", "notes_nonce", "notes_tag") 

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Login, LoginAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(PIN, PINAdmin)
admin.site.register(SecureNote, SecureNoteAdmin)
