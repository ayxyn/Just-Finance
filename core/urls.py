from django.urls import path
from django.views.generic import TemplateView

from . import views

# urlpatterns = [
#     path("", views.BaseIndexView.as_view(), name="index"),
#     path("about/", views.AboutView.as_view(), name="about"),
#     path("contact/", views.ContactView.as_view(), name="contact"),
# ]