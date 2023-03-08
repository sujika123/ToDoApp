
from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login',views.login,name='login')
    path('log',views.log,name='log'),
    path('admin',views.admin,name='admin'),
    path('userhome',views.userhome,name='userhome'),
    path('register',views.register,name='register'),
    path('user',views.user,name='user'),
    path('profile',views.profile,name='profile'),
    path('profileview',views.profileview,name='profileview'),
    path('profileupdate/<int:id>/',views.profileupdate,name='profileupdate'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('viewevent',views.viewevent,name='viewevent'),
    path('addevent',views.addevent,name='addevent'),
    path('eventupdate/<int:id>/',views.eventupdate,name='eventupdate'),
    path('eventdelete/<int:id>/', views.eventdelete, name='eventdelete'),



]

