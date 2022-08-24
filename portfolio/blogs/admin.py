from django.contrib import admin
from .models import BlogModel,Category,AppUser

# Register your models here.
admin.site.register(Category)
admin.site.register(AppUser)


class BlogAdminSchema(admin.ModelAdmin):
    list_display = ('title','ratings','category')
    list_per_page = 1

admin.site.register(BlogModel,BlogAdminSchema)