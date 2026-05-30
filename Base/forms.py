from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import Contact

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].min_length = 2
        self.fields['name'].max_length = 30
        self.fields['name'].widget.attrs.update({'placeholder':'Enter your name'})
        self.fields['email'].min_length = 5
        self.fields['email'].max_length = 50
        self.fields['email'].widget.attrs.update({'placeholder':'Enter your email'})
        self.fields['number'].min_length = 3
        self.fields['number'].max_length = 10
        self.fields['number'].widget.attrs.update({'placeholder':'Enter your number'})
        self.fields['message'].min_length = 10
        self.fields['message'].max_length = 500
        self.fields['message'].widget.attrs.update({'placeholder':'Enter your message'})