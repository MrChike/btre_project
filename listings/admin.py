from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published',
                    'price', 'list_date', 'realtor']
    # To be able to access the links via admin
    list_display_links = ['id', 'title']
    list_filter = ['realtor']
    list_editable = ['is_published']
    search_fields = ['title', 'description',
                     'address', 'city', 'state', 'zip_code', 'price']
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
