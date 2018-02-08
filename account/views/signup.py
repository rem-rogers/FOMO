from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import request
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone


@view_function
def process_request(request):

#process the form
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            #do the work of the form
            #create the user, etc.
            return HttpResponseRedirect('/')

    else:
        form = signUpForm()

#render the template
    context = {
        'form': form,
    }
    return request.dmp_render('signup.html', context)


class signUpForm(forms.Form):
    email= forms.CharField(label='Email')
