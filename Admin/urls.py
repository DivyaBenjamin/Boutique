from django.urls import path
from Admin import views
app_name="adminboutique"
urlpatterns = [
    path('adminboutique/',views.adminboutique,name="adminboutique"),
    path('Userreg/',views.userreg,name="userreg"),
    path('Staffreg/',views.staffreg,name="staffreg"),
    path('Styles/',views.styles,name="styles"),
    path('deletesty/<int:aid>',views.deletesty,name="deletesty"),
    path('typesofstyle/',views.typesofstyle,name="typesofstyle"),
    path('deletetypesof/<int:bid>',views.deletetypesof,name="deletetypesof"),
]