from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['website', 'username', 'password']

    def clean(self):
        cleaned_data = super(EntryForm, self).clean()
        website = cleaned_data.get('website')

        if website and not website.startswith('http://'):
            website = 'http://' + website
            cleaned_data['website'] = website

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.TextInput(attrs={'autocomplete': 'current-password'})
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete': 'username'})
