from django import forms
from registeration.models import user,system
class LoginForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length=100,widget=forms.EmailInput())
    password = forms.CharField(widget = forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        dbuser = user.objects.filter(name = name)
        dbemail = user.objects.filter(email= email)
        if dbuser:
            raise forms.ValidationError("username already exit.use another username")
        if dbemail :
            raise forms.ValidationError("email already exist in the system, use anoter one")
        if password != re_password:
            raise forms.ValidationError("password doesnot match,type again")
        new_user = user()
        new_user.name = name
        new_user.email = email
        new_user.password = password
        #new_user.save()

        return new_user

