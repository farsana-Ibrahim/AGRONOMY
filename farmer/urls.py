from farmer.models import *
from django.urls import path
from . import views

urlpatterns = [
      path('farmer_signup',views.farmer_signup,name="farmer_signup"),
      path('msg',views.msg,name="msg"),
      path('farmer_login',views.farmer_login,name="farmer_login"),
      path('fhome',views.fhome,name="fhome"),
      path('logout',views.logout,name="logout"),
      path('krishiall',views.krishiall,name='krishiall'),     
      path('km<int:id>',views.krishimain,name='km'),

      path('krishiprodall<str:pk>',views.krishiprodall,name='krishiprodall'),
      path('prodDview<int:id>',views.proddetailview,name='prodDview'),
      path('cf<str:pk>',views.categfilter,name='cf'),  
      
      path('agrolist',views.agrolist,name='agroli'),  
      path('agromain<int:id>',views.agromain,name='agromain'),  

      path('aprodD<int:id>',views.prodDview,name='aprodD'),
      path('acf<str:pk>',views.agroCategfilter,name='acf'),  

      path('cart',views.cart,name="cart"),
      path('acartdelete<int:aid>',views.adelete,name="acartdelete"),
      path('delete<int:kid>',views.delete,name="delete"),


      path('checkout<int:fid>',views.checkout,name="checkout"),

      path('rpay',views.razorpay,name='rpay'),

      path('payondlvry',views.payondelivery,name='payondlvry'),

      path('orderstatus',views.orderstatus,name="orderstatus"),

      path('echoshop',views.echoshop,name='echoshop'),

      path('echoaddpro',views.echoaddpro,name='echoaddpro'),


      path('echoprod',views.echoprod,name='echoprod'),

      path("eproview<int:did>",views.eproview, name="eproview"),
      path("eupprod<int:id>",views.eupprod,name="eupprod"),
      path("edelete<int:id>",views.edelete,name="edelete"),
      path('estatus',views.estatus,name='estatus'),
      path('fconfirm<str:pk>',views.confirmpayment,name='fconfirm'),


]
      