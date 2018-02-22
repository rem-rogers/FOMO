import re
from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import request
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

from catalog.models import Product
from formlib import Formless
from catalog import models as cmod
from django.contrib.auth import authenticate, login


@view_function
def process_request(request):

#process the form
    form = createProductForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('#')

#render the template
    context = {
        'form': form,
    }
    return request.dmp_render('#', context)


class createProductForm(Formless):

    def init(self):
        #product attributes
        type = forms.ChoiceField(choices=Product.TYPE_CHOICES, label="Type")
        status = forms.ChoiceField(choices=Product.STATUS_CHOICES, label='Status')
        name = forms.CharField(label="Name")
        description = forms.CharField()
        category = forms.ModelChoiceField(
            queryset=cmod.Category.objects.all(),
            label="category")
        price = forms.IntegerField(label="Price")
        quantity = forms.IntegerField(label="Quantity", required="False")
        reorder_trigger = forms.IntegerField(label="Reorder Trigger", required="False")
        reorder_quantity = forms.IntegerField(label="Reorder Quantity", required="False")
        pid = forms.CharField(label="Product ID", required="False")
        max_rental_days = forms.IntegerField(Label="Max Rental Days", required="False")
        retire_date = forms.DateTimeField(label="Retire Date", required="False")
        created_date = forms.DateTimeField(label="Created Date")
        last_modified = forms.DateTimeField(label="Last Modified")








