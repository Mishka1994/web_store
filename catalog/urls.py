from django.urls import path

from catalog.views import user_controller, user_contact_page

urlpatterns = [
    path('', user_controller),
    path('', user_contact_page),
]
