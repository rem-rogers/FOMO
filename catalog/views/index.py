from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod
import math


@view_function
def process_request(request, cat_id=0, pNum=1):
    category = cat_id
    cat = cmod.Category.objects.all()
    if category != 0:
        page = cmod.Product.objects.filter(category_id=cat_id).count()
    else:
        page = cmod.Product.objects.all().count()
    page = page/6
    page = math.ceil(page)

    currentPage = page

    context = {
        'cat': cat,
        jscontext('category'): category,
        jscontext('pNum'): pNum,
        jscontext('pMax'): page,
        'page': page,
        'currentPage': currentPage,
    }
    return request.dmp.render('index.html', context)

@view_function
def products(request, cat: cmod.Category=None, pnum: int=1):
    # qry = cmod.Product.objects.all()
    if cat is not None:
        qry = cmod.Product.objects.filter(category_id=cat.id)
        cName = cat
    else:
        qry = cmod.Product.objects.all()
        cName = 'All Products'

    qry = qry[((pnum - 1)*6):6*pnum] #pagination

    context = {
        'qry': qry,
        'pnum': pnum,
        'cName': cName,
    }
    return request.dmp.render('index.products.html', context) #inherits from base_ajax