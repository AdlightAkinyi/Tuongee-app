from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tubonge.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path(r'tubonge/', include('tubonge.urls')),
    path('', include('tubonge.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)