from django import forms
from .models import Work
from datetime import datetime

class WorkForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), initial=datetime.now)
    class Meta:
        model = Work
        fields = ['work_name', 'start_time', 'end_time', 'category']
