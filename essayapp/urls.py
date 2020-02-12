from django.urls import path,include
from . import views 

urlpatterns=[
    #path('',views.home1,name='home1'),
    #path('register',views.register,name='register'),
    #path('pali',views.pali,name='pali')
    #path('login',views.login,name='login'),
    #path('logout',views.logout,name='logout'),
    #path('booking',views.booking,name='booking')

    path('submit',views.submit,name='submit'),
    path('',views.index,name='index.html'),
    
]