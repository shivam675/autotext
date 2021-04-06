from django.forms import ModelForm
from .models import Automate_text

class TimetableForm(ModelForm):
    class Meta:
        model = Automate_text
        fields = ['title', 'message', 'number',  'important']
