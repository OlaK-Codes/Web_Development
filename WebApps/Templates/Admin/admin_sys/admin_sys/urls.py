"""
URL configuration for admin_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django .conf import settings
#to create own admin for cms
from CMS.admin import cms_site

urlpatterns = [
    path('my-unique-admin', admin.site.urls),
    #to create own url for admin in cms
    path('cms-admin/', cms_site.urls),

    #captha
    path('captcha/', include('captcha.urls')),

    # csv file data into admin db
    path('datawizard/', include('data_wizard.urls')),
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
