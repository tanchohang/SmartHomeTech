from django import forms
from .models import Message, MessageFiles, Reply, Project
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class QuotesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body', 'summary']


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ["subject", "body"]


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = MessageFiles
        fields = ['files']
        widgets = {
            'files': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class AppointmentForm(forms.Form):

    date = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '2020-01-1',
                'maxDate': '2023-01-1',
            },
        ),
        initial='2020-01-01',
    )
    time = forms.TimeField(
        widget=TimePicker(
            options={
                'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )

    CHOICES = [('skype', 'Skype'),
               ('phone', 'Phone')]

    preference = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={
            'placeholder': 'phone',
            'class': 'form-control'
        }))
