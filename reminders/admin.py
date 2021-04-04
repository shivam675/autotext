from django.contrib import admin
from .models import Automate_text
# Register your models here.
class AutomateAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Automate_text, AutomateAdmin)
