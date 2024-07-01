from django import forms
from api.models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'