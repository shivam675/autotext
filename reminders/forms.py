from django.forms import ModelForm
from .models import Automate_text

class TimetableForm(ModelForm):
    class Meta:
        model = Automate_text
        fields = ['title', 'message_to_send', 'number',  'important']
