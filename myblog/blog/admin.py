from django.contrib import admin
from blog.models import Category,Post



class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','url','image','add_date')
    search_fields=('title',)


class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','url','image')   
    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)