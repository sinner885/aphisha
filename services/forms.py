from django.forms import ModelForm
from .models import Service


class ServiceCreateForm(ModelForm):
    '''форма добавления сервисов'''
    class Meta:
        model = Service
        fields = ("category", "brend", "subject", "description",
            "images", "location", "name", "email", "telefon", "moderation")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-group',
                'autocomplete': 'off'
            })