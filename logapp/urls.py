from django.urls import path
from logapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home, name= 'vhome'),
    path('regis', views.register, name='Register'),
    path('log', views.userlogin, name='user_login'),
    path('logo', views.ulogout, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
