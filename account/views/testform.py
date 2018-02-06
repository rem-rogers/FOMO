from django import forms
from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):

    if request.method == 'POST':
        form = TestForm(request.POST)

    else:
        form = TestForm()

    context = {
        'form': form,
    }

    return request.dmp_render('testform.htm', context)




class TestForm(forms.Form):
    fav_ice_cream = forms.CharField(label='Favorite Ice Cream')
    renewal_date = forms.CharField(label='Renewal', help_text="Enter a date between now and 4 weeks (default3).")