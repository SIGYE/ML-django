from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tenant, HousingApplication, RentalPayment
from django.urls import reverse_lazy
from .forms import HousingApplicationForm
from django.db.models import Count, Sum
from django.db.models import Count, Sum, Case, When, Value, DecimalField
from django.db.models.functions import Coalesce
from django.shortcuts import render
from .models import Tenant



def home(request):
    return render(request, 'housing/home.html')

class TenantListView(ListView):
    model = Tenant
    template_name = 'housing/tenant_list.html'

class  TenantDetailView(DetailView):
    model = Tenant
    template_name = 'housing/tenant_detail.html'    

class TenantCreateView(CreateView):
    model = Tenant
    fields = ['name', 'email', 'phone_number']
    template_name = 'housing/tenant_form.html'
    success_url = reverse_lazy('tenant_list')

class TenantUpdateView(UpdateView):
    model = Tenant
    fields = ['name', 'email', 'phone_number']       
    template_name = 'housing/tenant_form.html'
    success_url = reverse_lazy('tenant_list')

class TenantDeleteView(DeleteView):
    model = Tenant
    template_name = 'housing/tenant_confirm_delete.html'
    success_url = reverse_lazy('tenant_list')    


class HousingApplicationListView(ListView):
    model = HousingApplication
    template_name = 'housing/housing_application_list.html'

class HousingApplicationDetailView(DetailView):
    model = HousingApplication
    template_name = 'housing/housing_application_detail.html'

class HousingApplicationCreateView(CreateView):
    model = HousingApplication
    form_class = HousingApplicationForm  
    template_name = 'housing/housing_application_form.html'
    success_url = reverse_lazy('housing_application_list')

class HousingApplicationUpdateView(UpdateView):
    model = HousingApplication
    form_class = HousingApplicationForm 
    template_name = 'housing/housing_application_form.html'
    success_url = reverse_lazy('housing_application_list')

class HousingApplicationDeleteView(DeleteView):
    model = HousingApplication
    template_name = 'housing/housing_application_confirm_delete.html'
    success_url = reverse_lazy('housing_application_list')


class RentalPaymentListView(ListView):
    model = RentalPayment
    template_name = 'housing/rental_payment_list.html'

class RentalPaymentDetailView(DetailView):
    model = RentalPayment
    template_name = 'housing/rental_payment_detail.html'    

class RentalPaymentCreateView(CreateView):
    model = RentalPayment
    fields = ['tenant', 'amount', 'payment_date']  
    template_name = 'housing/rental_payment_form.html'
    success_url = reverse_lazy('rental_payment_list')

class RentalPaymentUpdateView(UpdateView):
    model = RentalPayment
    fields = ['tenant', 'amount', 'payment_date']  
    template_name = 'housing/rental_payment_form.html'
    success_url = reverse_lazy('rental_payment_list')

class RentalPaymentDeleteView(DeleteView):
    model = RentalPayment
    template_name = 'housing/rental_payment_confirm_delete.html'
    success_url = reverse_lazy('rental_payment_list')

def statistics(request):
    try:
        
        tenant_names = list(
            Tenant.objects.values_list('name', flat=True)
            .order_by('name')  
        )
        
        application_counts = list(
            Tenant.objects.annotate(
                count=Coalesce(
                    Count('housingapplication'),
                    Value(0),
                    output_field=DecimalField()
                )
            ).values_list('count', flat=True)
            .order_by('name')  
        )
        
        total_payments = list(
            Tenant.objects.annotate(
                total=Coalesce(
                    Sum('rentalpayment__amount'),
                    Value(0),
                    output_field=DecimalField()
                )
            ).values_list('total', flat=True)
            .order_by('name')  
        )
        
        print("Tenant Names:", tenant_names)
        print("Application Counts:", application_counts)
        print("Total Payments:", total_payments)
        
        if len(tenant_names) != len(application_counts) or len(tenant_names) != len(total_payments):
            raise ValueError("Data length mismatch")
        context = {
            'tenant_names': tenant_names,
            'application_counts': application_counts,
            'total_payments': total_payments,
        }
        return render(request, 'housing/statistics.html', context)
    except Exception as e:
        
        print(f"Error in statistics view: {str(e)}")
        context = {
            'tenant_names': [],
            'application_counts': [],
            'total_payments': [],
            'error_message': 'Unable to load statistics at this time.'
        }
        return render(request, 'housing/statistics.html', context)