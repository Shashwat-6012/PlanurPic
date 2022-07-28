from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "Home page"),
    path("test/", views.test, name = "Test page"),
    path("PV", views.Productviewer, name = "Product page")
]