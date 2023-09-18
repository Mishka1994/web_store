from django.shortcuts import render


def user_controller(request):
    return render(request, 'catalog/home.html')


def user_contact_page(request):
    return render(request, 'catalog/contact_info.html')
