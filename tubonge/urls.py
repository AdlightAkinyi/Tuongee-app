from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url


urlpatterns = [
    path('', views.index, name='index'),
    path('navbar', views.nav, name='nav'),
    path('about',views.about,name='about'),
    path('footer',views.footer,name='footer'),
    path('contact',views.contact,name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'django-registration/logout.html')),
    
    path('homepage/', views.homepage,name='homepage'),
    url('profile/<id>/', views.profile, name='user_profile'),
    url('profile_update/<str:username>/', views.profile_update, name='profile_update'),
    url('<id>/', views.post_details, name='post_details'),
    url('create_post/new/', views.create_post, name='create_post'),
]
    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   