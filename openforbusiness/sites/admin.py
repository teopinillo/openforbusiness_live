from django.contrib import admin

from sites.models import BusinessClasification, BusinessIcon, Business, ColorScheme

class BusinessClasificationAdmin (admin.ModelAdmin):
    pass

class BusinessIconAdmin (admin.ModelAdmin):
    pass

class BusinessAdmin (admin.ModelAdmin):
    pass

class ColorSchemeAdmin (admin.ModelAdmin):
    pass

admin.site.register ( BusinessClasification, BusinessClasificationAdmin)
admin.site.register ( BusinessIcon, BusinessIconAdmin)
admin.site.register ( Business, BusinessAdmin )
admin.site.register ( ColorScheme, ColorSchemeAdmin )