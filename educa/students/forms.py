from django import forms

from courses.models import Course


class CourseEnrollFrom(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)
