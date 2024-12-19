from django import forms
from .models import TodoItem

# Create custom widget in your forms.py file.
class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class TodoCreateForm(forms.ModelForm):
    due_date = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = TodoItem
        fields = ['task', 'due_date', 'prority']