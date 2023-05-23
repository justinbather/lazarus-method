from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.forms import User
from .models import CustomUser, Task, PatientTest, UserEntryPatientTest
from django.utils.translation import gettext_lazy as _

# 

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=100, required=True,
                            widget=forms.EmailInput
                            (attrs={'class':'username_input', 'placeholder':'email'}))
    first_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class':'firstname_input', 'placeholder':'first name'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput
                                (attrs={'class':'lastname_input', 'placeholder':'last name'}))
    password1 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput
                                (attrs={'class':'password_input', 'placeholder':'password'}))
    password2 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput
                                (attrs={'class':'password_input', 'placeholder':'verify password'}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name')

class UserForm(forms.ModelForm):
    email= forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'class':'username_input', 'placeholder':'Email'}))
    password = forms.CharField(max_length=30,
                                widget=forms.PasswordInput
                                (attrs={'class':'password_input', 'placeholder':'Password'}))
    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class TestForm(forms.ModelForm):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDERS = [
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    ]

    gender = forms.CharField(required=True, widget=forms.Select(choices=GENDERS))
    exam_number = forms.IntegerField(widget = forms.HiddenInput(), initial=1)
    patient = forms.ModelChoiceField(queryset=CustomUser.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = UserEntryPatientTest
        fields = ["fasting_glucose", "hga1c", "cprotein", "homocysteine", "fasting_insulin", "ldl_particle", "ldl_size",
        "insulin_resistance", "testosterone", "thyroid", "vitamin_d3", "vitamin_b12", "zinc_rbc", "magnesium_rbc", "omega3_index", "exam_number", "weight", "height", "age", "gender", "patient"]
