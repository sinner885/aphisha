from django import forms
from .models import Advert



class AdvertCreateForm(forms.ModelForm):
    '''форма добавления объяв. на сайте'''
    class Meta:
        model = Advert
        fields = ('category', 'subject', 'types_ad',
                 'types_pr', 'description', 'images',
                 'name', 'email', 'telefon', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-group',
                'autocomplete': 'off'
            })
