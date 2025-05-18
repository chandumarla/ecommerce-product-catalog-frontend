import requests # type: ignore
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

API_BASE = 'https://chandumarla.pythonanywhere.com/api/products/'

def product_list_view(request):
    response = requests.get(API_BASE)
    products = response.json() if response.status_code == 200 else []
    return render(request, 'catalog/product_list.html', {'products': products})

def product_detail_view(request, pk):
    response = requests.get(f"{API_BASE}{pk}/")
    product = response.json() if response.status_code == 200 else None
    return render(request, 'catalog/product_detail.html', {'product': product})

def get_auth_headers():
    token = getattr(settings, 'ADMIN_API_TOKEN', None)
    if token:
        return {'Authorization': f'Token {token}'}
    return {}

@user_passes_test(lambda u: u.is_staff)
def add_product_view(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'description': request.POST.get('description'),
        }
        files = {'images': request.FILES['images']} if 'images' in request.FILES else {}
        headers = get_auth_headers()
        resp = requests.post(API_BASE, data=data, files=files, headers=headers)
        print(resp.status_code, resp.text)  # Debug line
        return redirect('product_list')
    return render(request, 'catalog/add_edit_product.html', {'title': 'Add Product'})

@user_passes_test(lambda u: u.is_staff)
def edit_product_view(request, pk):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'description': request.POST.get('description'),
        }
        files = {'images': request.FILES['images']} if 'images' in request.FILES else {}
        headers = get_auth_headers()
        requests.put(f"{API_BASE}{pk}/", data=data, files=files, headers=headers)
        return redirect('product_list')
    product = requests.get(f"{API_BASE}{pk}/").json()
    return render(request, 'catalog/add_edit_product.html', {'product': product, 'title': 'Edit Product'})

@user_passes_test(lambda u: u.is_staff)
def delete_product_view(request, pk):
    if request.method == 'POST':
        headers = get_auth_headers()
        requests.delete(f"{API_BASE}{pk}/", headers=headers)
        return redirect('product_list')
    product = requests.get(f"{API_BASE}{pk}/").json()
    return render(request, 'catalog/confirm_delete.html', {'product': product})