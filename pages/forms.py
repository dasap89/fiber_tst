# make sure this is at the top if it isn't already
# from django import forms
from pages.models import ContactModel
from django.forms import ModelForm

# our new form
# class ContactForm(forms.Form):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']