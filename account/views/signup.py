import re
from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import request
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from formlib import Formless
from account import models as amod
from django.contrib.auth import authenticate, login


@view_function
def process_request(request):

#process the form
    form = signUpForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/index')

#render the template
    context = {
        'form': form,
    }
    return request.dmp_render('signup.html', context)


class signUpForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label='Email', required=True)
        self.fields['first_name'] = forms.CharField(label='First Name', required=True)
        self.fields['last_name'] = forms.CharField(label='last Name', required=True)
        self.fields['address'] = forms.CharField(label='Address', required=True)
        self.fields['city'] = forms.CharField(label='City', required=True)
        self.fields['state'] = forms.CharField(label='State', required=True)
        self.fields['zip'] = forms.CharField(label='Zip', required=True)
        self.fields['password'] = forms.CharField(label='Enter Password', widget=forms.PasswordInput, required=True)
        self.fields['password2'] = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name

    def clean_address(self):
        address = self.cleaned_data.get('address')
        return address

    def clean_city(self):
        city = self.cleaned_data.get('city')
        return city

    def clean_state(self):
        state = self.cleaned_data.get('state')
        return state

    def clean_zip(self):
        zip = self.cleaned_data.get('zip')
        return zip

    def clean_password(self):
        password = self.cleaned_data.get('password')
        num = re.search('\d', password)
        if len(password) < 8 or num is None:
            raise forms.ValidationError('Password must be 8 characters or longer and contain a number')
        return password


    def commit(self):
        newuser = amod.User()
        newuser.email = self.cleaned_data.get('email')
        newuser.set_password(self.cleaned_data.get('password'))
        newuser.address = self.cleaned_data.get('address')
        newuser.city = self.cleaned_data.get('city')
        newuser.state = self.cleaned_data.get('state')
        newuser.zip = self.cleaned_data.get('zip')
        newuser.save()
        self.user = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))

        if self.user is None:
            raise forms.ValidationError('Invalid email or Password')
        return self.cleaned_data
        login(self.request, self.user)

    def clean(self):
         p1 = self.cleaned_data.get('password')
         p2 = self.cleaned_data.get('password2')
         if p1 != p2:
            raise forms.ValidationError('Please ensure the passwords match')
         return self.cleaned_data
    #     self.user.authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
    #     return self.cleaned_data



