from django import forms
# Create your models here.

class ContactForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    maps_link = forms.CharField()
    area = forms.CharField(max_length=100)
    permission_required = forms.BooleanField(required=False)
    contact_management_name = forms.CharField(max_length=100)
    contact_management_num = forms.CharField(max_length=100)