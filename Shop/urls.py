from django.urls import path
from Shop import views
app_name="shopboutique"
urlpatterns = [
    path('shopboutique/',views.shopboutique,name="shopboutique"),
    path('Addingstyles/',views.addingstyles,name="addingstyles"),
    path('Ajaxstyles/',views.Ajaxstyles,name="Ajaxstyles"),
    path('Addinghair/',views.addinghair,name="addinghair"),
    path('deletehair/<int:aid>',views.deletehair,name="deletehair"),
    path('Ajaxcut/',views.Ajaxcut,name="Ajaxcut"),
    path('Addingcolor/',views.addingcolor,name="addingcolor"),
    path('deletehaircolor/<int:bid>',views.deletehaircolor,name="deletehaircolor"),
    path('Ajaxcolor/',views.Ajaxcolor,name="Ajaxcolor"),
]