from django.contrib import admin
from .models import Fire, Satellite


class FireAdmin(admin.ModelAdmin):
    exclude = ('geometry',)

admin.site.register(Fire, FireAdmin)
admin.site.register(Satellite)
