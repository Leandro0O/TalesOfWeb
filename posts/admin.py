from django.contrib import admin
from .models import * 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author','created','update','categoria','description')
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Imagens)    
