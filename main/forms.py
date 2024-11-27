from django import forms
from markdown_it.rules_inline import image

from main.models import Course,UserSay,CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Course,Teacher

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'email', 
 
            'password1', 
            'password2'
        )  # Parol maydonlari allaqachon UserCreationForm orqali kiritiladi

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'image', 'price', 'start_time', 'end_time', 'schedule_days','teacher']

    # teacher maydonini formada ko'rsatmaslik
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), required=False)



class UserSayForm(forms.ModelForm):
    class Meta:
        model = UserSay
        fields = ['message']  # Faqat foydalanuvchi kirita oladigan maydon

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user  # Foydalanuvchini qo'shish
        if commit:
            instance.save()
        return instance
    
