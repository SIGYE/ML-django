from django.contrib import admin
from .models import Tenant, HousingApplication, RentalPayment

admin.site.register(Tenant)
admin.site.register(HousingApplication)
admin.site.register(RentalPayment)
