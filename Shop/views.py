from django.shortcuts import render,redirect
from Shop.models import *
# Create your views here.
def shopboutique(request):
    return render(request,'Shop/Home.html')

def addingstyles(request):
    stylesdata=tbl_styles.objects.all()
    typesofstyledata=tbl_typesof.objects.all()
    if request.method=="POST":
        sty=tbl_styles.objects.get(id=request.POST.get('Styles'))
        typesof=tbl_typesof.objects.get(id=request.POST.get('typesof'))
        tbl_addingstyles.objects.create(name=request.POST.get('name'),rate=request.POST.get('rate'),image=request.FILES.get('image'),typesof=typesof)
        return render(request,'Shop/Addingstyles.html')
    else:
        return render(request,'Shop/Addingstyles.html',{'sty':stylesdata,'typesof':typesofstyledata})

def Ajaxstyles(request):
    styles=tbl_styles.objects.get(id=request.GET.get('pisd'))
    typesofstyle=tbl_typesof.objects.filter(styles=styles)
    return render(request,'Shop/Ajaxstyles.html',{'typesof':typesofstyle})

def addinghair(request):
    haircutdata=tbl_haircuts.objects.all()
    typesofhaircutdata=tbl_typesofhair.objects.all()
    if request.method=="POST":
        haircut=tbl_haircuts.objects.get(id=request.POST.get('haircuts'))
        typesofhair=tbl_typesofhair.objects.get(id=request.POST.get('typesofhair'))
        tbl_addinghair.objects.create(name=request.POST.get('name'),rate=request.POST.get('rate'),image=request.FILES.get('image'),haircuts=haircut,typesofhair=typesofhair)
        return render(request,'Shop/Addinghair.html')
    else:
        return render(request,'Shop/Addinghair.html',{'haircuts':haircutdata,'typesofhair':haircutdata})

def Ajaxcut(request):
    haircut=tbl_haircuts.objects.get(id=request.GET.get('cisd'))
    typesofhair=tbl_typesofhair.objects.filter(haircuts=haircut)
    return render(request,'Shop/Ajaxcut.html',{'typesofhair':typesofhair})

def deletehair(request,aid):
     tbl_haircoloring.objects.get(id=aid).delete()
     return redirect('shopboutique:addinghair')

def addingcolor(request):
    haircoloringdata=tbl_haircoloring.objects.all()
    typesofcolordata=tbl_typesofcoloring.objects.all()
    if request.method=="POST":
        haircoloring=tbl_haircoloring.objects.get(id=request.POST.get('haircoloring'))
        typesofcolor=tbl_typesofcoloring.objects.get(id=request.POST.get('typesofhair'))
        tbl_addingcoloring.objects.create(name=request.POST.get('name'),rate=request.POST.get('rate'),image=request.FILES.get('image'),haircoloring=haircoloring,typesofhair=typesofcolor)
        return render(request,'Shop/Addingcolor.html')
    else:
        return render(request,'Shop/Addingcolor.html',{'haircoloring':haircoloringdata,'typesofhair':typesofcolordata})

def deletehaircolor(request,bid):
    tbl_addingcoloring.objects.get(id=bid).delete()
    return redirect('shopboutique:addingcolor') 

def Ajaxcolor(request):
    haircoloring=tbl_haircoloring.objects.get(id=request.GET.get('hisd'))
    typesofcoloring=tbl_typesofcoloring.objects.filter(typesofhair=haircoloring)
    return render(request,'Shop/Ajaxcolor.html',{'addingcoloring':typesofcoloring})