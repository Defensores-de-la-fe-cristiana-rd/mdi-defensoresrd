from django.contrib import admin
from .models import junta_directiva
# Register your models here.

class juntaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(junta_directiva, juntaAdmin)
