from django.forms import ModelForm

from chatapp.models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('label',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['label'].widget.attrs.update({'style':'width: 100%;'})
        