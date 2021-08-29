from django.contrib import admin

from sites.models import BusinessClasification, BusinessIcon, Business

class BusinessClasificationAdmin (admin.ModelAdmin):
    pass

class BusinessIconAdmin (admin.ModelAdmin):
    pass

class BusinessAdmin (admin.ModelAdmin):
    pass

admin.site.register ( BusinessClasification, BusinessClasificationAdmin)
admin.site.register ( BusinessIcon, BusinessIconAdmin)
admin.site.register ( Business, BusinessAdmin )