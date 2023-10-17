from django.urls import path
from Userboutique import views
app_name="Userboutique"
urlpatterns = [
    path('Userboutique/',views.Userboutique,name="Userboutique"),
    path('Styles/',views.styles,name="styles"),
]