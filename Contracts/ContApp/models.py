from django.core.validators import RegexValidator
from pickle import NONE
from django.db import models
from django.db.models import Max
# Create your models here.

class Vendors(models.Model):
    contractee_vendor=models.CharField(max_length=30, unique=True)
    company=models.CharField(max_length=30)
    description=models.TextField(blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number=models.CharField([phoneNumberRegex], max_length = 16, unique = True, blank=True)
    def __str__(self):
        return self.contractee_vendor
    

class assets(models.Model):
    producto=models.CharField(max_length=30, unique=True)
    Repara= 'RP'
    Uso='US'
    Bodega='BD'
    estado_CHOICES= [
        (Repara, 'En Reparacion'),
        (Uso, 'En Uso'),
        (Bodega, 'En Bodega'),
        ]
    estdo=models.CharField(
        max_length=2,
        choices=estado_CHOICES,
        default=None,
        )
    def is_upperclass(self):
        return self.estdo in {self.Repara, self.Uso}
    codigo=models.CharField(max_length=20)
    donde=models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.producto


class Contratos(models.Model):
    name=models.CharField(max_length=30)
    contractor=models.ForeignKey(Vendors, on_delete=models.CASCADE)
    contractee=models.CharField(max_length=30)
    start=models.DateField()
    end=models.DateField()
    cost=models.DecimalField(max_digits=9, decimal_places=2)
    blank=''
    Pesos= 'PE'
    Dolares='DL'
    CURR_CHOICES= [
        (blank, '----'),
        (Pesos, 'MXN'),
        (Dolares, 'DLLS'),
        ]
    currency=models.CharField(
        max_length=2,
        choices=CURR_CHOICES,
        default=None,
        )
    def is_upperclass(self):
        return self.currency in {self.Pesos, self.Dolares}
    Producto12='PR'
    Servicio= 'SE'
    Poliza='PO'
    Lic='LC'
    Otro='OT'
    TIPO_CHOICES= [
        (blank, '----'),
        (Producto12, 'Product'),
        (Servicio, 'Service'),
        (Poliza, 'Policy'),
        (Lic, 'Licensing'),
        (Otro, 'Other'),
        ]
    type=models.CharField(
        max_length=2,
        choices=TIPO_CHOICES,
        default=None,
        )
    def is_upperclass(self):
        return self.type in {self.Servicio, self.Otro}
    description =models.TextField(blank=True)
    product=models.ForeignKey(assets,
        on_delete=models.CASCADE, blank=True)
    attached_file=models.FileField(upload_to="media", blank=True)
    notification=models.BooleanField(default=False)
    def __str__(self):
        return self.name


