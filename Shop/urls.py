from django.urls import path
from Shop import views
app_name="shopboutique"
urlpatterns = [
    path('shopboutique/',views.shopboutique,name="shopboutique"),
    path('Profile/',views.profile,name="profile"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('Viewassigned/',views.viewassigned,name="viewassigned"),
    path('logout/',views.logout,name="logout"),
]