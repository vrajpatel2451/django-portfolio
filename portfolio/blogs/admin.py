from django.contrib import admin
from .models import BlogModel,Category,AppUser,Person,Book

# Register your models here.
admin.site.register(Category)
admin.site.register(AppUser)
admin.site.register(Person)
admin.site.register(Book)


class BlogAdminSchema(admin.ModelAdmin):
    list_display = ('title','ratings','category')
    list_per_page = 1

admin.site.register(BlogModel,BlogAdminSchema)