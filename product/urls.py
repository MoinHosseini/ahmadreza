from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",views.home,name="home-page"),

    path("all/<str:type>",views.all,name="all"),

    ### the below url is being used for adding new materials to the database
    path("add/",login_required(views.add.as_view()),name="add-material"),
    
    path("addtocart/",login_required(views.CartView.as_view()) ,name="add-to-cart"),

    path("create/",views.create,name="create"),

    path("check/",views.checkcart,name="check-cart"),

    path("remove/<str:type>/<int:id>",views.remove,name="remove"),
    path("edit/<int:id>/",views.edit),
    path("alter/<int:id>/",views.alter),

    path("report/material",views.report),
    
    path("report/kala",views.report2),

    path("factor/<str:type>",views.factor),
    path("addtofactor/",views.factoring),
    path("checkfactor/",views.checkfactor),
    path("removefcart/<int:id>",views.removefcart),
    path("view/<int:id>",views.factor_content),

    path("notif/<str:type>",views.notif),
]