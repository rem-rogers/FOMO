from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request, prodid: cmod.Product, cat_id=0):

    prod = prodid
    img = prod.image_urls()
    category = cat_id
    cat = cmod.Category.objects.all()

    context = {
        'prod': prod,
        'img': img,
        'cat': cat,
    }

    return request.dmp.render('detail.html', context)