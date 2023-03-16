from django import forms
from html import escape

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
#     your_email = forms.EmailField(label='Your Email', max_length=100)
#     message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    your_email = forms.EmailField(label='Your Email', max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean_your_name(self):
        # uses html escape for sanitation
        data = self.cleaned_data['your_name']
        return escape(data)
