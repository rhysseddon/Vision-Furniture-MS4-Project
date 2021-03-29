from django import forms
from .models import Product, Room


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rooms = Room.objects.all()
        friendly_names = [(r.id, r.get_friendly_name()) for r in rooms]

        self.fields['room'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
