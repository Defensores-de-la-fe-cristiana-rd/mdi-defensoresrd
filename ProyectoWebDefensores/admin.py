from django.contrib import admin
from .models import Noticias, Post, Contactanos, ImagenCarrusel
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Noticias, HomeAdmin)

admin.site.register(Post)
admin.site.register(Contactanos)
admin.site.register(ImagenCarrusel  )
