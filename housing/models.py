from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class HousingApplication(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected')

    ])

    def __str__(self):
        return f"{self.tenant.name} - {self.amount}"
    
class RentalPayment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.tenant.name} - {self.amount}"    