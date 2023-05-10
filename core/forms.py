from django.forms import ModelForm
from django import forms
from core.models import Mility, Voting
from django.core.exceptions import ValidationError

class MilitiForm(ModelForm):
    
    class Meta:
        model = Voting
       
        fields = ('name', 'number_voting')
        
        wdgets = {
        'name':  forms.TextInput(attrs={'class':'py-4 px-6  w-80'}),
        'number_voting':  forms.NumberInput(attrs={'class':'py-4 px-6 w-80 ' })
        }
       
       
    
    def clean_number_voting(self):
        number_voting = self.cleaned_data['number_voting']
        if number_voting == 0 or number_voting >= 2 :
           raise ValidationError('vous devez voté en 1 chiffre Ni 2')
            
        return number_voting
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if  'udc' not in name and 'Mrc' not in name :
            raise forms.ValidationError('vous devez entez le de un parti de poltique')
        if 'rpdc' not in  name:
            raise forms.ValidationError('vous devez entez le de un parti de poltique')
        return name