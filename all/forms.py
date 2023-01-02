from django import forms

from all.models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'message')
