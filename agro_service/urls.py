from krishibhavan.models import *
from django.urls import path
from .import views

urlpatterns = [
    path('agro_reg',views.agro_reg,name="agro_reg"),
    path('agro_login',views.agro_login,name="agro_login"),
    path('logout',views.logout,name='logout'),
    
    path('agrohome',views.agro_home,name="agrohome"),

    path('A_categ',views.addCateg,name='A_categ'),

    path('A_Addpro',views.Addpro,name='A_Addpro'),
    
    path('allp',views.allprod,name='allp'),
    
    path('catf<str:pk>',views.Cfilter,name='catf'),

    path('status',views.status,name='status'),

    path('agroconfirm<str:pk>',views.confirmpayment,name='agroconfirm'),


    path("aprodDview<int:did>",views.aprodDview, name="aprodDview"),

    path("aupprod<int:id>",views.aupprod,name="aupprod"),

    path("adelete<int:id>",views.adelete,name="adelete"),


    
]