from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='ShopHome'),#this "" means from mac url.py /shop directive
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("product/<int:myid>", views.product, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
