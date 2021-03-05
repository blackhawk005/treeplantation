from django import forms
# Create your models here.

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=100)
    date = forms.DateField()
    time = forms.TimeField()
    place = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)