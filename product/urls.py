from django.urls import path
from . import views

urlpatterns = [
    path("all/",views.all,name="all-products"),
    path("add/",views.add.as_view(),name="add-products"),
]