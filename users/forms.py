from django import forms
from users.models import User, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)
        
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email",]
        
