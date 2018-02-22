from django.db import models
from django_mako_plus import view_function
from catalog import models as cmod

@view_function
def process_request(request, product:cmod.Product):
#name = cmod.