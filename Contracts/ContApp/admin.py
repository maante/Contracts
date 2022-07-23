from django.contrib import admin
from .models import Contratos, Vendors, assets


admin.site.register(Contratos)
admin.site.register(Vendors)
admin.site.register(assets)

# Register your models here.
