from django import forms
# Create your models here.

class EventForm(forms.Form):
    date = forms.DateField()
    # maps_link = forms.CharField()
    # area = forms.CharField(max_length=100)
    # permission_required = forms.BooleanField(required=False)
    # contact_management_name = forms.CharField(max_length=100)
    # contact_management_num = forms.CharField(max_length=100)
class GeeksForm(forms.Form): 
    geeks_field = forms.DateField( ) 