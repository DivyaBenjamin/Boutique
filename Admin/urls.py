from django.urls import path
from Admin import views
app_name="adminboutique"
urlpatterns = [
    path('adminboutique/',views.adminboutique,name="adminboutique"),
    path('Servicestype/',views.servicestypes,name="servicestypes"),
    path('deleteservices/<int:bid>',views.deleteservices,name="deleteservices"),
    path('Addservices/',views.addservices,name="addservices"),
    path('deleteaddservice/<int:cid>',views.deleteaddservice,name="deleteaddservice"),
    path('Work/',views.work,name="work"),
    path('deletework/<int:aid>',views.deletework,name="deletework"),
    path('Staffreg/',views.staffreg,name="staffreg"),
    path('Adminreg/',views.adminreg,name="adminreg"),
    path('Assignstaff/<int:did>',views.assignstaff,name="assignstaff"),
    path('Viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('stafflist/<int:eid>',views.stafflist,name="stafflist"),
    path('Viewbooking/',views.viewbooking,name="viewbooking"),
    path('Assignwork/',views.assignwork,name="assignwork"),
    path('serviceserializer/',views.serviceserializer),
    path('serviceserializer/<int:eid>',views.upserviceserializer),
]