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
        return HttpResponseRedirect('/catalog/productList')

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
        self.fields['description'] = forms.CharField(label="description", required=True)
        self.fields['category'] = forms.ModelChoiceField(
            queryset=cmod.Category.objects.all(),
            label="category")
        self.fields['price'] = forms.IntegerField(label="Price")

        #bulk
        self.fields['quantity'] = forms.IntegerField(label="Quantity", required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label="Reorder Trigger", required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label="Reorder Quantity", required=False)

        #
        self.fields['pid'] = forms.CharField(label="Product ID", required=False)
        self.fields['max_rental_days'] = forms.IntegerField(label="Max Rental Days", required=False)
        self.fields['retire_date'] = forms.DateTimeField(label="Retire Date", required=False)

    def clean(self):
        type = self.cleaned_data.get('type')
        if type == 'BulkProduct':
            quantity = self.cleaned_data.get('quantity')
            reorder_trigger = self.cleaned_data.get('reorder_trigger')
            reorder_quantity = self.cleaned_data.get('reorder_quantity')
            bulk = [quantity, reorder_trigger, reorder_quantity]
            for b in bulk:
                if b == None:
                    raise forms.ValidationError('Field is required')
            return self.cleaned_data
        elif type == 'IndividualProduct':
            pid = self.cleaned_data.get('pid')
            if pid is None:
                raise forms.ValidationError('Field is required')
            return self.cleaned_data
        elif type == 'RentalProduct':
            pid = self.cleaned_data.get('pid')
            max_rental_days = self.cleaned_data.get('max_rental_days')
            retire_date = self.cleaned_data.get('retire_date')
            rentals = [pid, max_rental_days, retire_date]
            for r in rentals:
                if r == None:
                    raise forms.ValidationError('Field is required')
            return self.cleaned_data

    def commit(self):
        type = self.cleaned_data.get('type')
        if self.type == 'BulkProduct':
            self.product = cmod.BulkProduct()
            self.product.create_date = self.cleaned_data.get('created_date')
            self.product.last_modified = self.cleaned_data.get('last_modified')
            self.product.name = self.cleaned_data.get('name')
            self.product.description = self.cleaned_data.get('description')
            self.product.status = self.cleaned_data.get('status')
            self.product.category = self.cleaned_data.get('category')
            self.product.price = self.cleaned_data.get('price')
            #unique
            self.product.quantity = self.cleaned_data.get('quantity')
            self.product.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            self.product.reorder_quantity = self.cleaned_data.get('reorder_quantity')

        elif self.type == 'IndividualProduct':
            self.product = cmod.IndividualProduct()
            self.product.create_date = self.cleaned_data.get('created_date')
            self.product.last_modified = self.cleaned_data.get('last_modified')
            self.product.name = self.cleaned_data.get('name')
            self.product.description = self.cleaned_data.get('description')
            self.product.status = self.cleaned_data.get('status')
            self.product.category = self.cleaned_data.get('category')
            self.product.price = self.cleaned_data.get('price')
            #unique
            self.product.pid = self.cleaned_data.get('pid')

        elif self.type == 'RentalProduct':
            self.product = cmod.RentalProduct()
            self.product.create_date = self.cleaned_data.get('created_date')
            self.product.last_modified = self.cleaned_data.get('last_modified')
            self.product.name = self.cleaned_data.get('name')
            self.product.description = self.cleaned_data.get('description')
            self.product.status = self.cleaned_data.get('status')
            self.product.category = self.cleaned_data.get('category')
            self.product.price = self.cleaned_data.get('price')
            #unique
            self.product.pid = self.cleaned_data.get('pid')
            self.product.max_rental_days = self.cleaned_data.get('max_rental_days')
            self.product.retire_date = self.cleaned_data.get('retire_date')
        self.product.save()







