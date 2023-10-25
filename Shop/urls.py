from django.urls import path
from Shop import views
app_name="shopboutique"
urlpatterns = [
    path('shopboutique/',views.shopboutique,name="shopboutique"),
    path('Addingstyles/',views.addingstyles,name="addingstyles"),
    path('Ajaxstyles/',views.Ajaxstyles,name="Ajaxstyles"),
    path('Staffreg/',views.staffreg,name="staffreg"),
    path('Addinghair/',views.addinghair,name="addinghair"),
    path('Ajaxcut/',views.Ajaxcut,name="Ajaxcut"),
]