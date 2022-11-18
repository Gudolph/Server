from django.contrib import admin
from .models import Letter

# Register your models here.
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display= ('id', 'user', 'title', 'body', 'is_public', 'created_at')