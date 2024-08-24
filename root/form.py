from django import forms
from .models import Newsletter, Contactus

class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
    
class Contactusform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['name','email','subject','message']