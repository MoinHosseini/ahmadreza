from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",views.home,name="home-page"),

    path("all/<str:type>",views.all,name="all"),

    path("add/",login_required(views.add.as_view()),name="add-material"),
    path("addtocart/",login_required(views.CartView.as_view()) ,name="add-to-cart"),
    path("create/",views.create,name="create"),
    path("check/",views.checkcart,name="check-cart"),

    path("remove/<str:type>/<int:id>",views.remove,name="remove"),
    path("edit/<int:id>/",views.edit),
    path("alter/<int:id>/",views.alter),

    path("report/material",views.report,name="materialreport"),
    path("report/kala",views.report2,name="kalareport"),

    path("factor/<str:type>",views.factor,name="factor"),
    path("addtofactor/",views.factoring,name="addtofactor"),
    path("checkfactor/",views.checkfactor,name="checkfactor"),
    path("removefcart/<int:id>",views.removefcart),
    path("view/<int:id>",views.factor_content , name="view"),

    path("notif/<str:type>",views.notif,name="notif"),
]