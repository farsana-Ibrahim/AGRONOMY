from client.models import *
from django.urls import path
from . import views

urlpatterns = [
    
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('chome',views.chome,name="chome"),
    path('logout',views.logout,name="logout"),
    path('echoall',views.echoall,name='echoall'),     
    path('km<int:id>',views.echomain,name='fm'),
    path('echoprodall<str:fk>',views.echoprodall,name='echoprodall'),
    path('eprodD<int:id>',views.eprodDview,name='eprodD'),
    path('ecart',views.ecart,name="ecart"),
    path('cdelete<int:eid>',views.cdelete,name="cdelete"),
    path('echeckout<int:cid>',views.echeckout,name="echeckout"),
    path('epay',views.razorpay,name='epay'),
    path('payondlvry',views.payondelivery,name='payondlvry'),
    path('orderstatus',views.orderstatus,name="orderstatus"),
]