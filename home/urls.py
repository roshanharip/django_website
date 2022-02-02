from django.urls import path, include
from home import views       
urlpatterns = [
    path('',views.index,name="index"),
    path("index",views.index,name="index"),
    path("login",views.login,name='login'),
    path("logout",views.logoutuser,name="logout"),
    path("create",views.createone,name='createone'),
    path('validation',views.validation,name="validation"),
    path('otp',views.otp,name="otp"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('about',views.about,name="about"),
    path("attendance",views.attendance,name="attendance"),
    path('library',views.library,name="library"),
    path('notice',views.notice,name="notice"),
    path('payment',views.payment,name="payment"),
    path('registration',views.registration,name="registration")
]