from django.contrib import admin

from sites.models import BusinessClasification, Business, ColorScheme, PersonFavorite, BusinessReview

class BusinessClasificationAdmin (admin.ModelAdmin):
    pass

class BusinessAdmin (admin.ModelAdmin):
    pass

class ColorSchemeAdmin (admin.ModelAdmin):
    pass

class PersonFavoriteAdmin (admin.ModelAdmin):
    pass

class BusinessReviewAdmin (admin.ModelAdmin):
    pass

admin.site.register ( BusinessClasification, BusinessClasificationAdmin)
admin.site.register ( Business, BusinessAdmin )
admin.site.register ( ColorScheme, ColorSchemeAdmin )
admin.site.register ( PersonFavorite, PersonFavoriteAdmin )
admin.site.register ( BusinessReview, BusinessReviewAdmin )