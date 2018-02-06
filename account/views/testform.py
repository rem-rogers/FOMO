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

    return request.dmp_render('testform.html', context)




class TestForm(forms.Form):

    def init(self):
        self.fields['fav_ice_cream'] = forms.CharField(label='Favorite Ice Cream')
        self.fields['age'] = forms.IntegerFieldField(label='Age')
        self.fields['renewal_date'] = forms.CharField(label='Renewal', help_text="Enter a date between now and 4 weeks (default3).")

    @property
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            print('too young') #don't allow sign up
        return age
