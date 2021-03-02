from django import forms
# Create your models here.

class EventForm(forms.Form):
    date = forms.DateField()
    time = forms.CharField(max_length=100)
    place = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)