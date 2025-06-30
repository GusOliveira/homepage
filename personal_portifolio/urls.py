"""personal_portifolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portifolio import views # Keep this for other views if any, or adjust if new_home is the only one from portifolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'), # Old homepage
    path('', views.new_home, name='new_home'), # New homepage
    path('blog/', include('blog.urls')),
    # You might want to keep the old home page accessible at a different URL for a while:
    # path('old-home/', views.home, name='old_home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)