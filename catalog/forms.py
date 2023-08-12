from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, ProductVersion


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


def forbidden_words_validator(value):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                       'полиция', 'радар']
    for word in forbidden_words:
        if word.lower() in value.lower():
            raise ValidationError(f'В моем доме попрошу не выражаться! Убери - "{word}"!')


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('category',)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['name'].validators.append(forbidden_words_validator)
    self.fields['description'].validators.append(forbidden_words_validator)


class ProductVersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = '__all__'
