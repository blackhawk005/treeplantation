from django import forms
from .models import *


class ImageForm(forms.Form):
    image = forms.ImageField(label='Image')