from django.forms import ModelForm
from models import Task
from models import SIZE_CHOICES
from django.forms.widgets import RadioSelect
from django.forms.fields import ChoiceField

class InboxForm(ModelForm):
    class Meta:
        model = Task
        exclude=['size','is_blocked','is_archived','is_delayed','project']

class TaskForm(ModelForm):
    size = ChoiceField(widget=RadioSelect, choices=SIZE_CHOICES, label='Magnitud')
    class Meta:
        model = Task
