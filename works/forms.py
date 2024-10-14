from django import forms
from datetime import datetime
from .models import Work

class WorkForm(forms.ModelForm):
    
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = Work
        fields = ['work_name', 'category']