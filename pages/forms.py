from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your Name')
    email= forms.EmailField()
    massage = forms.CharField(widget=forms.Textarea)

    