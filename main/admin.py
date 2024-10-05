from django.contrib import admin

from main.models import category, product

admin.site.register(category)



@admin.register(product)
class prodactadmin(admin.ModelAdmin):
    list_display = ("name", "coust", "quantity", "category",)