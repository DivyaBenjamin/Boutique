from django.urls import path
from Shop import views
app_name="shopboutique"
urlpatterns = [
    path('shopboutique/',views.shopboutique,name="shopboutique"),
]