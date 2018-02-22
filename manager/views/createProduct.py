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
        return HttpResponseRedirect('/')

#render the template
    context = {
        'form': form,
    }
    return request.dmp_render('createProduct.html', context)


class createProductForm(Formless):

    def init(self):
        #product attributes
        self.fields['type'] = forms.ChoiceField(choices=Product.TYPE_CHOICES, label="Type")
        self.fields['status'] = forms.ChoiceField(choices=Product.STATUS_CHOICES, label='Status')
        self.fields['name'] = forms.CharField(label="Name", required=True)
        self.fields['description'] = forms.CharField(labe="description", required=True)
        self.fields['category'] = forms.ModelChoiceField(
            queryset=cmod.Category.objects.all(),
            label="category")
        self.fields['price'] = forms.IntegerField(label="Price")

        #bulk
        self.fields['quantity'] = forms.IntegerField(label="Quantity", required="False")
        self.fields['reorder_trigger'] = forms.IntegerField(label="Reorder Trigger", required="False")
        self.fields['reorder_quantity'] = forms.IntegerField(label="Reorder Quantity", required="False")

        #
        self.fields['pid'] = forms.CharField(label="Product ID", required="False")
        self.fields['max_rental_days'] = forms.IntegerField(label="Max Rental Days", required="False")
        self.fields['retire_date'] = forms.DateTimeField(label="Retire Date", required="False")

    def clean(self):
        type = self.cleaned_data.get('type')
        if type == 'bulk product':
            quantity = self.cleaned_data.get('quantity')
            reorder_trigger = self.cleaned_data.get('reorder_trigger')
            reorder_quantity = self.cleaned_data.get('reorder_quantity')
        else if type == 'Individual Product':
            pid = self.cleaned_data.get('pid')
        else if




