from django import forms
from userin.models import UserProfileInfo,LookingCab,BookedCab
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','name','mobile')

class LookingCabForm(forms.ModelForm):
    date = forms.DateField(
        label='Date',
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    class Meta():
        model = LookingCab
        fields = ('date','source','dest')

class BookedCabForm(forms.ModelForm):
    date = forms.DateField(
        label='Date',
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    class Meta():
        model = BookedCab
        fields = ('date','source','dest',)