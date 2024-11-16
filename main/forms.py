from django import forms
from markdown_it.rules_inline import image

from main.models import Course,User


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = '__all__'
        
        
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['full_name','email','password']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
