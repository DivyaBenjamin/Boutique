from django.urls import path
from Admin import views
app_name="adminboutique"
urlpatterns = [
    path('adminboutique/',views.adminboutique,name="adminboutique"),
    path('Userreg/',views.userreg,name="userreg"),
    path('Styles/',views.styles,name="styles"),
    path('deletesty/<int:aid>',views.deletesty,name="deletesty"),
    path('typesofstyle/',views.typesofstyle,name="typesofstyle"),
    path('deletetypesof/<int:bid>',views.deletetypesof,name="deletetypesof"),
    path('Shopreg/',views.shopreg,name="shopreg"),
    path('Haircuts/',views.haircuts,name="haircuts"),
    path('deletehair/<int:cid>',views.deletehair,name="deletehair"),
    path('typesofhaircut/',views.typesofhaircut,name="typesofhaircut"),
    path('deletetypeshair/<int:did>',views.deletetypeshair,name="deletetypeshair"),
    path('Adminreg/',views.adminreg,name="adminreg"),
    path('Haircoloring/',views.haircoloring,name="haircoloring"),
    path('deletecoloring/<int:eid>',views.deletecoloring,name="deletecoloring"),
]