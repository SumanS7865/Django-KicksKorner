from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account, UserProfile
import re


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "form-control"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "phone_number", "email", "password"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        # Use regular expression to check if the phone number contains only digits

        if len(phone_number) < 8:
            raise forms.ValidationError(
                "phone number must be at least 8 characters long."
            )

        if not re.match(r"^\d+$", phone_number):
            raise forms.ValidationError("Phone number should contain only digits.")

        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get("password")

        # Check if the password meets the requirements
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        if not re.search(r"[A-Z]", password):
            raise forms.ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"\d", password):
            raise forms.ValidationError(
                "Password must contain at least one numeric digit."
            )
        if not re.search(r"[@#$%^&+=]", password):
            raise forms.ValidationError(
                "Password must contain at least one special character (@, #, $, %, ^, &, +, or =)."
            )

        return password

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "Enter First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email Address"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Enter Phone Number"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "phone_number")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        error_messages={"invalid": ("Image files only")},
        widget=forms.FileInput,
    )

    class Meta:
        model = UserProfile
        fields = (
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "country",
            "profile_picture",
        )

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
