from django import forms
from markdown_it.rules_inline import image

from main.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = '__all__'
