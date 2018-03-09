from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod


@view_function
def process_request(request, cat_id=0):
    category = cat_id
    cat = cmod.Category.objects.all()
    context = {
        'cat': cat,
        jscontext('category'): category,
        jscontext('pnum'): 1,
    }
    return request.dmp.render('index.html', context)

@view_function
def products(request, cat: cmod.Category=None, pnum: int=1):
    # qry = cmod.Product.objects.all()
    if cat is not None:
        qry = cmod.Product.objects.filter(category_id=cat.id)
    else:
        qry = cmod.Product.objects.all()

    qry = qry[((pnum - 1)*6):6*pnum] #pagination
    context = {
        'qry': qry,
        'pnum': pnum,
    }
    return request.dmp.render('index.products.html', context) #inherits from base_ajax