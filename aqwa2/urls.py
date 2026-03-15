"""aqwa2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aqwa2 import view




urlpatterns = [
    path('Adminpanel2/', admin.site.urls ,name='Adminpanel2'),
    path("Adminpanel/",view.Adminpanel ,name='Adminpanel'),

    path("",view.home ,name='view'),
    path("StudentEnroll/",view.StudentEnroll ,name='StudentEnroll'),
    path("View_Enroll_All/",view.View_Enroll_All ,name='View_Enroll_All'),
    
    path("registration/",view.registration ,name='registration'),

    
    path("vieww/",view.vieww ,name='vieww'),
    path("viewalldata/", view.viewalldata, name='viewalldata'),
    
    path("earchbatchtime/", view.earchbatchtime, name='earchbatchtime'),
    path("sendbatchtime/<str:inputbatchtime>",view.sendbatchtime ,name='sendbatchtime'),
    
    path("searchregistration/",view.searchregistration ,name='searchregistration'),
    path("registrationdata/<str:aqs>",view.registrationdata ,name='registrationdata'),

    path("searchbyname/",view.searchbyname ,name='searchbyname'),
    path("bynamedata/<str:byname>",view.bynamedata ,name='bynamedata'),
    
    # path("deletedata/<str:uid>/<str:Rpage>",view.deletedata ,name='ath'),
    
    
    path("deletedata/<int:uid>/<str:Rpage>/", view.deletedata, name="deletedata" ),
    path("passoutentry/",view.passoutentry ,name='passoutentry'),

    path("update/",view.update ,name='update'),
    path("updateuser/<str:regnodata>",view.updateuser ,name='updateuser'),

    path("fee/",view.fee ,name='fee'),
    path("submitfee/",view.submitfee ,name='submitfee'),
    path("submitfee2/<str:regno>",view.submitfee2, name='submitfee2'),
    path('PendingFEE/',view.PendingFEE, name='PendingFEE'),
    
    path("feeshistory/<int:id>/",view.feeshistory),

    path("passoutstudent/",view.passoutstudent ,name='passoutstudent'),
    path("passoutview/",view.passoutview ,name='passoutview'),
    
    path("updateuserpass/<str:regnodata>",view.updateuserpass ,name='updateuserpass'),
    path("deletepassout/<str:getid>/<str:Rpage>/",view.deletepassout ,name='deletepassout'),

    path("certificate/<str:registrationno>",view.certificate ,name='certificate'),
    
    path("Adminpanel/",view.Adminpanel ,name='Adminpanel'),
    path('login/',view.login, name='login'),
    path('signup/',view.signup, name='signup'),
    path('logout/',view.logout, name='logout'),
    # path("checkdeletedata/<str:deletedatabyreg>",view.checkdeletedata)
]


