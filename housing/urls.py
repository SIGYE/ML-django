from django.urls import path
from .views import (
    home,
    TenantListView, TenantDetailView, TenantCreateView, TenantUpdateView, TenantDeleteView,
    HousingApplicationListView, HousingApplicationDetailView, HousingApplicationCreateView, HousingApplicationUpdateView, HousingApplicationDeleteView,
    RentalPaymentListView, RentalPaymentDetailView, RentalPaymentCreateView, RentalPaymentUpdateView, RentalPaymentDeleteView,
    statistics
)

urlpatterns = [
    #Home URls
    path('', home, name='home'),
    

    path('tenants/', TenantListView.as_view(), name='tenant_list'),
    path('tenants/<int:pk>/', TenantDetailView.as_view(), name='tenant_detail'),
    path('tenants/create/', TenantCreateView.as_view(), name='tenant_create'),
    path('tenants/<int:pk>/edit/', TenantUpdateView.as_view(), name='tenant_edit'),
    path('tenants/<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),

    path('applications/', HousingApplicationListView.as_view(), name='housing_application_list'),
    path('applications/<int:pk>/', HousingApplicationDetailView.as_view(), name='housing_application_detail'),
    path('applications/create/', HousingApplicationCreateView.as_view(), name='housing_application_create'),
    path('applications/<int:pk>/edit/', HousingApplicationUpdateView.as_view(), name='housing_application_edit'),
    path('applications/<int:pk>/delete/', HousingApplicationDeleteView.as_view(), name='housing_application_delete'),

    path('payments/', RentalPaymentListView.as_view(), name='rental_payment_list'),
    path('payments/<int:pk>/', RentalPaymentDetailView.as_view(), name='rental_payment_detail'),
    path('payments/create/', RentalPaymentCreateView.as_view(), name='rental_payment_create'),
    path('payments/<int:pk>/edit/', RentalPaymentUpdateView.as_view(), name='rental_payment_edit'),
    path('payments/<int:pk>/delete/', RentalPaymentDeleteView.as_view(), name='rental_payment_delete'),

    path('statistics/', statistics, name='statistics'),
]
