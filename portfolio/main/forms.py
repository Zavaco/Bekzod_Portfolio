from django import forms
from .models import *
from django.forms import ModelForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['f_name', 'l_name', 'message']
        widgets = {
            'f_name': forms.TextInput(
                attrs={
                    'class': 'in_1',
                }
            ),
            'l_name': forms.TextInput(attrs={'class': 'in_2',
                                             }),
            'message': forms.TextInput(attrs={'class': 'in_3',
                                              }),



        }
