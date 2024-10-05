from django.shortcuts import render, HttpResponseRedirect
from main.models import  product, category, Bsket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def main(request):
    return render(request, 'main/main.html')

def pronas(request):
    return render(request, 'main/pronas.html' )

def magaz(request, category_id=None, page=1):
    products = product.objects.filter(category_id=category_id) if category_id else product.objects.all()

    per_page = 1000
    paginator = Paginator(products, per_page)
    product_paginator = paginator.page(page)

    context = {
        'category': category.objects.all(),
        'product': product_paginator
    }
    return render(request, 'main/magaz1.html', context)

@login_required
def bsket_add(request, product_id):
    product1 = product.objects.get(id=product_id)
    bskets = Bsket.objects.filter(user=request.user, product=product1,)

    if not bskets.exists():
        Bsket.objects.create(user=request.user, product=product1, quantity=1)
    else:
        bsket = bskets.first()
        bsket.quantity += 1
        bsket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def katalog(request):
    context = {
        'category': category.objects.all(),
    }
    return render(request, 'main/katalog.html', context)


def resume(request, product_id):
    context={
        'product': product.objects.filter(id=product_id) if id else product.objects.all()
    }
    return render(request, 'main/resume.html', context) 

def kontakt(request):
    return render(request, 'main/kontakt.html' )