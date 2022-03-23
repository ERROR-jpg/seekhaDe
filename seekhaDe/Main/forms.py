from django import forms
from django.contrib.auth.models import user
from Main.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = user,
        fields=('username','first_name','email','password1','password2')

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'student'),
        (parent, 'parent')
    ]
    user_type = forms.ChoiceField(required=True, choices= user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
    