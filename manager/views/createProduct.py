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
        return HttpResponseRedirect('/catalog/productList/')
    context = {
        'form': form,
    }
    return request.dmp.render('createProduct.html', context)


class createProductForm(Formless):

    def init(self):
        #product attributes
        self.fields['type'] = forms.ChoiceField(choices=cmod.Product.TYPE_CHOICES, label="Type", show_hidden_initial=True)
        self.fields['status'] = forms.ChoiceField(choices=cmod.Product.STATUS_CHOICES, label='Status', initial='A')
        self.fields['name'] = forms.CharField(label="Product Name", required=True)
        self.fields['description'] = forms.CharField(label="Product Description", required=True)
        self.fields['category'] = forms.ModelChoiceField(
            queryset=cmod.Category.objects.all(),
            label="category")
        self.fields['price'] = forms.IntegerField(label="Price")
        #bulk
        self.fields['quantity'] = forms.IntegerField(label="Quantity", required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label="Reorder Trigger", required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label="Reorder Quantity", required=False)
        #individual
        self.fields['pid'] = forms.IntegerField(label='Product ID', required=False)
        #rental
        self.fields['max_rental_days'] = forms.IntegerField(label="Max Rental Days", required=False)
        self.fields['retire_date'] = forms.DateTimeField(label="Retire Date", required=False)

        self.product = None

    def clean(self):
        type = self.cleaned_data.get('type')
        quantity = self.cleaned_data.get('quantity')
        reorder_trigger = self.cleaned_data.get('reorder_trigger')
        reorder_quantity = self.cleaned_data.get('reorder_quantity')
        pid = self.cleaned_data.get('pid')
        max_rental_days = self.cleaned_data.get('max_rental_days')
        retire_date = self.cleaned_data.get('retire_date')

        if type == 'BulkProduct':
            if quantity is None:
                raise forms.ValidationError('Quantity is required for Bulk Products')
            if reorder_trigger is None:
                raise forms.ValidationError('Reorder Trigger is required for Bulk Products')
            if reorder_quantity is None:
                raise forms.ValidationError('Reorder Quantity is required for Bulk Products')

        elif type == 'IndividualProduct':
            if pid is ' ':
                raise forms.ValidationError('Field is required')

        elif type == 'RentalProduct':
            if max_rental_days is None:
                raise forms.ValidationError('Max Rental Days is required for Rental Products')
            if pid == '':
                raise forms.ValidationError('Product ID is required for Rental Products')
            return self.cleaned_data

    def commit(self):
        type = self.cleaned_data.get('type')
        if type == 'IndividualProduct':
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
        elif type == 'BulkProduct':
            self.product = cmod.BulkProduct()
            self.product.create_date = self.cleaned_data.get('created_date')
            self.product.last_modified = self.cleaned_data.get('last_modified')
            self.product.name = self.cleaned_data.get('name')
            self.product.description = self.cleaned_data.get('description')
            self.product.status = self.cleaned_data.get('status')
            self.product.category = self.cleaned_data.get('category')
            self.product.price = self.cleaned_data.get('price')
            # unique
            self.product.quantity = self.cleaned_data.get('quantity')
            self.product.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            self.product.reorder_quantity = self.cleaned_data.get('reorder_quantity')
        elif type == 'RentalProduct':
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







