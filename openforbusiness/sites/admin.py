from django.contrib import admin

from sites.models import BusinessClasification, Business, ColorScheme, PersonFavorite

class BusinessClasificationAdmin (admin.ModelAdmin):
    pass

class BusinessAdmin (admin.ModelAdmin):
    pass

class ColorSchemeAdmin (admin.ModelAdmin):
    pass

class PersonFavoriteAdmin (admin.ModelAdmin):
    pass

admin.site.register ( BusinessClasification, BusinessClasificationAdmin)
admin.site.register ( Business, BusinessAdmin )
admin.site.register ( ColorScheme, ColorSchemeAdmin )
admin.site.register ( PersonFavorite, PersonFavoriteAdmin )