from django.contrib import admin
from mainapp.models import *

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    fields = ['name','phone', 'category', 'text','is_paid']
    list_display = ('name','phone', 'category', 'text','is_paid')
    list_display_links = ('name','phone')
    list_filter = ('category', 'is_paid')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'on_main_page', 'get_prev')
    list_display_links = ('title',)
    list_editable = ('on_main_page','order_sort')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('s_title', 'get_prev_icon', 'get_prev_sp_icon')
    list_display_links = ('s_title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title','author_name','get_prev')
    list_display_links = ('title',)

@admin.register(Form_section)
class ConsultationOrderAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'price')
    list_display_links = ('s_name',)
    list_editable = ('price',)

admin.site.register(MpHeadBlock1)
admin.site.register(MpHead)
admin.site.register(Ticker)
admin.site.register(Services_section)
admin.site.register(Scroll_menu_text)
admin.site.register(Bottom_footer)
admin.site.register(Page)
admin.site.register(Slider2)
