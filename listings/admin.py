from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  # to show columns for the listings table in the admin area
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  # to make the id and title links to the listing
  list_display_links = ('id', 'title')
  # to make a filter box
  list_filter = ('realtor',)
  # to make is_published editable
  list_editable =('is_published',)
  # to make a search bar and listing searchable
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  # create pagination
  list_per_page = 5

# Register your models here.
admin.site.register(Listing, ListingAdmin)