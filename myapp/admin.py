from django.contrib import admin
from .models import Contact , Subscribe


# Register your models here.

admin.site.register(Contact)
admin.site.register(Subscribe)


admin.site.site_header = "Price Comparison Admin"
admin.site.index_title = "Welcome to Price Compare"
admin.site.site_title = "Price Comparison website"