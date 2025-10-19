from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g., Intro to HCI"}),
            "code":  forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g., HCI-101"}),
        }

        def clean_code(self):
            code = self.cleaned_data["code"].strip()
            return code.upper()