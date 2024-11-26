from django.contrib import admin
from .models import Donor

#admin bcsedu/bcsedu

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'mobile_number', 'last_blood_donation', 'is_available','created_at')
    search_fields = ('name', 'blood_group', 'mobile_number','created_at')  # Optional: Adds a search box to filter by fields
    list_filter = ('blood_group', 'is_available')  # Optional: Adds filter options in the sidebar for these fields

admin.site.register(Donor, DonorAdmin)
