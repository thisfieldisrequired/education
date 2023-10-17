from django import forms
from courses.models import Course


class CourseEnrollForm(forms.Form):
    """Форма регистрации регистрация на курск"""

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), widget=forms.HiddenInput
    )
