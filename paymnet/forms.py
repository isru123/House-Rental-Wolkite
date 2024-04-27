from django import forms

class TenantInfoForm(forms.Form):
    id_document = forms.FileField(label='Identification Document', widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    tenant_photo = forms.FileField(label='Tenant Photo', widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
