from django import forms
from .models import Message, ProjectFiles, Project, Quote, Appointment
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

from crispy_forms.helper import FormHelper
import datetime


class QuotesForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['description']


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

    class Meta:
        model = Message
        fields = ["subject", "body"]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class FileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

    class Meta:
        model = ProjectFiles
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class AppointmentForm(forms.ModelForm):

    # date = forms.DateField(input_formats=['%Y-%m-%d'],
    #                        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    time = forms.TimeField(widget=forms.TimeInput(
        attrs={'class': 'timepicker', 'type': 'time'}))

    CHOICES = [('skype', 'Skype'),
               ('phone', 'Phone')]

    preference = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
    ))

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'preference']
        widgets = {
            'date': forms.DateInput(format=('%Y/%m/%d'), attrs={'type': 'date'}),
        }
