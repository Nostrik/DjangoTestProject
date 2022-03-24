from turtle import title
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class UploadValidFile(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()

    def is_valid_form(self):
        if self.description in ['слово', 'нельзя', 'использовать']:
            return False
        else:
            return True