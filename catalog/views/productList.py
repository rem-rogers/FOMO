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
    products = cmod.Product.objects.filter(status='A')
    context = {
        'products': products,
    }
    return request.dmp_render('productList.html', context)

