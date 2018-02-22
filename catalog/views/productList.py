# import re
# from django import forms
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from django.http import request
# from django_mako_plus import view_function, jscontext
# from datetime import datetime, timezone
# from catalog.models import Product
# from formlib import Formless
# from catalog import models as cmod
# from django.contrib.auth import authenticate, login
#
# @view_function
# def process_request(request, product:cmod.Product):
#
#     products = cmod.Product.objects.get(status='A')
#
#     form = editProductForm(request)
#     if form.is_valid():
#         form.commit()
#         return HttpResponseRedirect('/')
#
#
#     context = {
#         'form': form,
#     }
#     return request.dmp_render('productList.html', context)
#
# class editProdctForm(Formless):
#
#     def init(self):
#
