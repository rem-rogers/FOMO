import re
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django_mako_plus import view_function, RedirectException
from formlib import Formless
from account import models as amod

@view_function
def process_request(request):
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/index/')

    context = {
        'form': form,
    }
    return request.dmp_render('login.html', context)

class LoginForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(required=True)
        self.fields['password'] = forms.CharField(required=True, widget=forms.PasswordInput())
        self.user = None

    def clean(self):
        self.user = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))

        if self.user is None:
            raise forms.ValidationError('Invalid email or Password')
        return self.cleaned_data

    def commit(self):
        login(self.request, self.user)

