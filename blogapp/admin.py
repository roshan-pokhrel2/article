from django.contrib import admin
from .models import Articles, getintouch

class debug(admin.ModelAdmin):
    list_display =('username', 'title', 'description')
    list_filter = ('date', 'username')
admin.site.register(Articles, debug)






admin.site.register(getintouch)
