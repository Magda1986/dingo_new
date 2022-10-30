from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["value", "error"]

    def clean(self):
        cleaned_data = super().clean()

        print(cleaned_data)

        value = cleaned_data.get('value')
        error = cleaned_data.get('error')

        if cleaned_data['error'] == '':
            cleaned_data['error'] = None

        if value and error:
            raise forms.ValidationError("Podaj tylko jedną z wartości")
        elif not (value and error):
            raise forms.ValidationError("Nie podano żadnej wartości!")

        return cleaned_data
