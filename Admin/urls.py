from django.urls import path
from Admin import views
app_name="adminboutique"
urlpatterns = [
    path('adminboutique/',views.adminboutique,name="adminboutique"),
    path('Userreg/',views.userreg,name="userreg"),
    path('Staffreg/',views.staffreg,name="staffreg"),
]