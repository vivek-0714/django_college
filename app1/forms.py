from django import forms
from app1.models import students,deparments,faculty

class student_form(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'


class department_form(forms.ModelForm):
    class Meta:
        model=deparments
        fields='__all__'


class faculty_form(forms.ModelForm):
    class Meta:
        model=faculty
        fields='__all__'
