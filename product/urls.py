from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    path("all/<str:type>",views.all,name="all-products"),
    path("add/",views.add.as_view(),name="add-material"),
    path("addtocart/",views.CartView.as_view() ,name="add-to-cart"),
    path("check/",views.checkcart,name="check-cart"),
    path("remove/<int:id>",views.remove,name="remove"),
    path("create/",views.create,name="create"),
    path("edit/<int:id>/",views.edit),
    path("alter/<int:id>/",views.alter),
    path("report",views.report),
    path("factor",views.factor.as_view()),
]