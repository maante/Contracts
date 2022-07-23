from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContractsForm, vendorsform, assetsform, vendor_form, assets_form, RegisterForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from .models import Contratos, Vendors, assets
from django.contrib import messages
import json, datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth import login, logout, authenticate

# Create your views here.

@login_required
def contract_list(request):
    contract_list = Contratos.objects.all() 
    return render(request, "contracts.html", {'contract_list': contract_list})

@login_required
def contract_form(request):
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #term = request.GET.get('term')
        #contractors = Vendors.objects.all().filter(contractee_vendor__icontains=term)
        #return JsonResponse(list(contractors.values()), safe=False)
    form = ContractsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Form submission successful")
        return redirect('contracts')
    else:
        messages.error(request, "Error, contract not submitted")
    return render(request, 'contracts_form.html', {'form':form })

def contract_view(request, id):
    cont = Contratos.objects.get(pk=id)
    return render(request, 'contract_view.html', {'cont':cont})

def contract_edit(request,id):
    contratos = Contratos.objects.get(id=id)
    form = ContractsForm(request.POST or None, request.FILES or None, instance=contratos)
    if form.is_valid():
         form.save()
         messages.success(request, "Form submission successful")
         return redirect('contracts')
    return render(request,"contracts_form.html", {'form':form})

def contract_delete(request, id):
    contrato = Contratos.objects.get(pk=id)
    contrato.delete()
    return redirect('/contracts')

class VendorsModal(BSModalCreateView):
    template_name = 'vendform.html'
    form_class = vendorsform
    success_message = 'Success: Vendor created'
    success_url = reverse_lazy('new-contract')
   
def VendorsUpdate(request):
    data=dict()
    if request.method=='GET':
        vendor= Vendors.objects.all()
        data['instance'] = render_to_string('contracts.html', {'vendor':vendor}, request=request)
        return JsonResponse(data)


class AssetsModal(BSModalCreateView):
    template_name = 'productform.html'
    form_class = assetsform
    success_message = 'Success: Asset created'
    success_url = reverse_lazy('new-contract')



@login_required
def vendors_list(request):
    vendors_list = Vendors.objects.all()
    return render(request, "vendors.html", {'vendors_list': vendors_list})

@login_required
def vendor_formview(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = vendor_form()
        else:
            vendors = Vendors.objects.get(pk=id)
            form = vendor_form(instance=vendors)
        return render(request,"vendors_form.html", {'form':form})
    else:
        if id == 0:
            form = vendor_form(request.POST)
        else:
            vendors = Vendors.objects.get(pk=id)
            form = vendor_form(request.POST, instance= vendors)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submission successful")
        else:
            messages.error(request, "Error, contract not submitted")

        return redirect('/vendors')

@login_required
def vendor_delete(request, id):
    vend = Vendors.objects.get(pk=id)
    vend.delete()
    return redirect('/vendors')

@login_required
def asset_list(request):
    asset_list = assets.objects.all()
    return render(request, "assets.html", {'asset_list': asset_list})

@login_required
def asset_formview(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = assets_form()
        else:
            asse = assets.objects.get(pk=id)
            form = assets_form(instance=asse)
        return render(request, "assets_form.html", {'form':form})
    else:
        if id == 0:
            form = assets_form(request.POST)
        else:
            asse = assets.objects.get(pk=id)
            form = assets_form(request.POST, instance= asse)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submission successful")
        else:
            messages.error(request, "Error, contract not submitted")
        return redirect('/assets')

@login_required
def asset_delete(request, id):
    asst = assets.objects.get(pk=id)
    asst.delete()
    return redirect('/assets')

@login_required
def event(request):
    all_events = Contratos.objects.all().filter(notification=1)
    get_event_types = Contratos.objects.only('name')

    if request.GET:
        event_arr = []
        if request.GET.get('name') == "all":
            all_events = Contratos.objects.all()
        else:
            all_events = Contratos.objects.filter(name__icontains=request.GET.get('name'))


        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.name
            start_date = datetime.strptime(str(i.start.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.strptime(str(i.end.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HTTPResponse(json.dumps(event_arr))

    context = {
        "events": all_events,
        "get_event_types": get_event_types,

    }
    return render(request, 'index.html', context)

def sign_up(request):
    if request.method=='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign up successful")
            return redirect('login')

    else:
        form = RegisterForm()
        messages.error(request, "Error, signup not submitted, check password is the same and correct email domain")
    return render(request, 'registration/sign_up.html', {"form": form})