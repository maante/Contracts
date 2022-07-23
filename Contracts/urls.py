"""Contracts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from ContApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='index.html'), name='index'), #homepage
    path('', views.event, name = 'index'),
    path('accounts/', include('django.contrib.auth.urls')), #login/logout
    path('accounts/sign-up', views.sign_up, name= 'signup'), #signup
    path('contracts/', views.contract_list, name = 'contracts'), #shows contract table/list
    path('contracts/edit/<int:id>', views.contract_edit, name='edit'), #edit/update form
    path('contracts/add', views.contract_form, name = 'new-contract'), #add a contract
    path('contracts/view/<int:id>', views.contract_view, name='view-contract'),
    path('contracts/delete/<int:id>', views.contract_delete, name ='delete'),
    path('contracts/add/addvendor', views.VendorsModal.as_view(), name='new_vendor'), #add a vendor
    path('contracts/add/addasset', views.AssetsModal.as_view(), name='new_asset'),
    path('vendors/', views.vendors_list, name = 'vendors'), #Vendor table
    path('vendors/add', views.vendor_formview, name = 'add_vendor'),
    path('vendors/edit/<int:id>', views.vendor_formview, name='editvendor'),
    path('vendors/delete/<int:id>', views.vendor_delete, name ='delete-vendor'),
    path('assets/', views.asset_list, name = 'assets'),
    path('assets/add', views.asset_formview, name = 'add_asset'),
    path('assets/edit/<int:id>', views.asset_formview, name='edit-asset'),
    path('assets/delete/<int:id>', views.asset_delete, name ='delete-asset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

