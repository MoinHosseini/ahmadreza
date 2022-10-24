from django.urls import path
from . import views

urlpatterns = [
    path("all/",views.all,name="all-products"),
    path("add/",views.add.as_view(),name="add-material"),
    path("addtocart/",views.CartView.as_view() ,name="add-to-cart"),
    path("check/",views.checkcart,name="check-cart"),
    path("create/",views.create,name="create"),
    path("edit/<int:id>/",views.edit),
]