from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin


from .models import Slide


class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'order')


admin.site.register(Slide, SlideAdmin)
