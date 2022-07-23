from django import forms
from django.forms import TextInput, PasswordInput, ModelForm
from .models import Contratos, Vendors, assets
from django.forms.widgets import NumberInput
from bootstrap_modal_forms.forms import BSModalModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogINFO(forms.Form):
    username= forms.CharField(label= 'Usuario: ', max_length=20, widget=forms.TextInput(attrs={"placeholder": "Username", 'style': 'width: 300px;', "class": "form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            }
    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["waldorfastoria.com"]
        if domain not in domain_list:
            raise forms.ValidationError("Please enter an email address with a valid domain")
        return data
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contratos
        fields = '__all__'

        widgets = {
            
            'name': forms.TextInput(attrs ={'class': 'form-control'}),
            'contractor': forms.Select(attrs={'class': 'form-control', 'id': 'contractor_view' }),
            'contractee': forms.TextInput(attrs={'class': 'form-control'}),
            'start': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'currency':forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product_view'}),
            #'attached_file': forms.FileInput(attrs={'style': 'display: none'}),
            'notification': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.fields['contractor'].queryset = Vendors.objects.none()
        #self.fields['product'].queryset = assets.objects.none()
        #if 'contractor' in self.data:
           # self.fields['contractor'].queryset = Vendors.objects.all()

        #elif self.instance.pk:
            #self.fields['contractor'].queryset = Vendors.objects.all().filter(pk=self.instance.contractor.pk)


        

class vendorsform(BSModalModelForm):
    class Meta:
        model = Vendors
        fields = '__all__'

        widgets = {
            'contractee_vendor': forms.TextInput(attrs ={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            }

class assetsform(BSModalModelForm):
    class Meta:
        model = assets
        fields = '__all__'

        widgets = {
            'producto': forms.TextInput(attrs ={'class': 'form-control'}),
            'estdo': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'donde': forms.TextInput(attrs={'class': 'form-control'}),
            }        

class vendor_form(forms.ModelForm):
   class Meta:
        model = Vendors
        fields = '__all__'

        widgets = {
            'contractee_vendor': forms.TextInput(attrs ={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            }

class assets_form(forms.ModelForm):
    class Meta:
        model = assets
        fields = '__all__'

        widgets = {
            'producto': forms.TextInput(attrs ={'class': 'form-control'}),
            'estdo': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'donde': forms.TextInput(attrs={'class': 'form-control'}),
            }    

