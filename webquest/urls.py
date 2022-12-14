"""webquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('main.urls')),
    url(r'^taskone/', include('taskone.urls')),
    url(r'^tasktwo/', include('tasktwo.urls')),
    url(r'^taskthree/', include('taskthree.urls')),
    url(r'^taskfour/', include('taskfour.urls')),
    url(r'^taskfive/', include('taskfive.urls')),
    url(r'^kriteri/', include('kriteri.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^tasksix/', include('tasksix.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
