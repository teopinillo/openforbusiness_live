from django.contrib import admin

from sites.models import BusinessClasification, BusinessIcon

class BusinessClasificationAdmin (admin.ModelAdmin):
    pass

class BusinessIconAdmin (admin.ModelAdmin):
    pass

admin.site.register (BusinessClasification, BusinessClasificationAdmin)
admin.site.register (BusinessIcon, BusinessIconAdmin)
